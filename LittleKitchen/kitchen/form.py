from django.forms import Form,ModelForm,fields
from .models import User,UserInfo
from captcha.fields import CaptchaField
from django.contrib.auth import authenticate
from django.forms import PasswordInput,CharField
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import TextInput

############################  古耀华  登录注册     ##########################
#登录验证
class Login(Form):
    username=fields.CharField(max_length=20,label='用户名',widget=forms.TextInput(attrs={"placeholder":'请输入用户名'}))
    password=fields.CharField(max_length=20,label='密码',widget=PasswordInput(attrs={"placeholder":'请输入密码'}))
    # captcha=CaptchaField()
    def clean(self):
        data=super().clean()    #cleaded_data 干净数据
        name=data.get('username',None)
        password=data.get('password',None)
        print(name,password)
        if name and password:
            user=authenticate(username=name,password=password)
            self.user = user
            if not user:
                raise ValidationError("用户名或密码错误")
#注册验证
class Register(Form):
    captcha=CaptchaField(label='验证码')
    username=fields.CharField(max_length=11,label='手机号',widget=forms.TextInput(attrs={"placeholder":'请输入手机号'}))
    password = fields.CharField(max_length=20, label='密码', widget=forms.PasswordInput(attrs={"placeholder": '请输入密码'}))
    passwords = fields.CharField(widget=PasswordInput(attrs={"placeholder":"请再次输入您的密码"}), label="再次输入密码")
    def clean(self):
        data = super().clean()
        username=data.get('username',None)
        password=data.get('password',None)
        passwords=data.get('passwords',None)
        check = User.objects.filter(username=username).first()
        if check == None:
            if len(username) < 11:
                raise ValidationError("注册失败: 手机号不能少于11位")
        else:
            raise ValidationError("注册失败: 用户名已注册")

##############################################################################


# class Register(Form):
#     name=CharField(label="用户名",max_length=11,widget=forms.TextInput(attrs={"placeholder":"请在此填写您的手机号码"}))
#     def clean(self):
#         data = super().clean()
#         name = data.get("name", None)
#         check=User.objects.filter(username=name).first()
#         if check == None:
#             length=len(name)
#             if length < 11:
#                 raise ValidationError("手机号不能少于11位")
#         else:
#             raise ValidationError("用户名已注册")
#
# class Register1(Form):
#     name=CharField(label="用户名",max_length=20,widget=forms.TextInput(attrs={"placeholder":"请填写您的用户名"}))
#     password = CharField(label="密码",widget=forms.PasswordInput(attrs={"placeholder":"请在此设置您的密码"}))
#     password2 = CharField(widget=PasswordInput(attrs={"placeholder":"请再次输入您的密码"}), label="再次输入密码")
#     def clean(self):
#         data2 = super().clean()
#         print("datadata2",data2)
#         name2 = data2.get("name", None)
#         psd = data2.get("password", None)
#         psd2 = data2.get("password2", None)
#         print(name2,psd,psd2)
#         checkname=Info.objects.filter(nickname=name2).first()
#         print(checkname)
#         if checkname == None:
#             if psd != psd2:
#                 raise ValidationError("两次密码不一致")
#         else:
#             raise ValidationError("昵称已存在，请换一个")