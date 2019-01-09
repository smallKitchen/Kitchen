from django.shortcuts import render,reverse,redirect
from .form import Login,Register
from django.contrib.auth import login as login1
from .models import User,UserInfo
# Create your views here.

# 闪屏页一
def index_one(request):
    return render(request,'kitchen/flash1.html')
# 闪屏页二
def index_two(request):
    return render(request,'kitchen/flash2.html')


#############################  薛维嘉  智能组菜   ######################################

# 前台首页
def index(request):
    return render(request,'kitchen/index.html')


########################################################################################



############################# 古耀华 ################################
#登录
def login(request):
    if request.method=="GET":
        form=Login()
        return render(request,"kitchen/login.html",{'form':form})
    else:
        form = Login(request.POST)
        if form .is_valid():
            print("验证成功")
            login1(request,form.user)
            return redirect(reverse('kitchen:index'))
        else:
            form =Login()
            return redirect(reverse('kitchen:login'),{'form':form})


#注册
def register(request):
    if request.method=="POST":
        form=Register(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            User.objects.create_user(username=data['username'],password=data['password'])
            return redirect("kitchen:register")
        else:
            return render(request, "kitchen/G_register.html", {'form': form})
    else:
        form=Register()
        return render(request,"kitchen/G_register.html",{'form':form})

########################################################################