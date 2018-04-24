from django.db import models
from db_model.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser, BaseModel):
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'blog_user'
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name


class UserInfo(BaseModel):
    user = models.OneToOneField(User, verbose_name='用户名', on_delete=models.CASCADE)
    qq_id = models.CharField(max_length=15, verbose_name='QQ账号')
    wechat_id = models.CharField(max_length=50, verbose_name='微信账号')
    github_id = models.CharField(max_length=50, verbose_name='GitHub账号')
    weibo_id = models.CharField(max_length=50, verbose_name='微博账号')
    introduction = models.CharField(max_length=250, verbose_name='个人简介')
    name = models.CharField(max_length=30, verbose_name='昵称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_userinfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
