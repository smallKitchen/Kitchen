from django.db import models
from db.basemodels import BaseModel
from django.contrib.auth.models import User

# Create your models here.
# 用户表
class UserInfo(BaseModel):
    name = models.OneToOneField(to=User, default="", on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='手机号')
    type = models.IntegerField(verbose_name='类型',choices=(
        (0,'用户'),
        (1,'商家')
    ),default=0)
    photo = models.ImageField(verbose_name='头像',default='')
    follow = models.IntegerField(verbose_name='关注量',default=0)
    class Meta:
        verbose_name_plural = "用户表"

# 菜谱表
class Menu(models.Model):
    name = models.CharField(verbose_name='菜名',max_length=50)
    img = models.ImageField(verbose_name='图像',default='')
    ingres = models.TextField(verbose_name='食材',max_length=50)
    step = models.TextField(verbose_name='步骤',max_length=3000)
    score = models.IntegerField(verbose_name='评分')
    bq = models.CharField(verbose_name='标签',max_length=50,default='')
    class Meta:
        verbose_name_plural = "菜谱表"

# 动态表
class Dynamic(BaseModel):
    author = models.CharField(verbose_name='发布者',max_length=20)
    con = models.TextField(verbose_name='动态内容',max_length=1000)
    z_number = models.IntegerField(verbose_name='获赞量')
    class Meta:
        verbose_name_plural = "动态表"

# 评论表
class Comment(BaseModel):
    author = models.CharField(verbose_name='评论者',max_length=20)
    con = models.TextField(verbose_name='评论内容',max_length=1000)
    u_id = models.IntegerField(verbose_name='被评论者ID')
    class Meta:
        verbose_name_plural = "评论表"

