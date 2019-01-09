from django.db import models

class BaseModel(models.Model):
    c_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True) #创建时间
    u_time = models.DateTimeField(verbose_name='更新时间',auto_now=True) #更新时间
    del_id = models.BooleanField(verbose_name='是否删除',default=False) #是否删除
    class Meta:
        #说明是抽象模型类
        abstract =True