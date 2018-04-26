# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='github_id',
            field=models.CharField(verbose_name='GitHub账号', blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='introduction',
            field=models.CharField(verbose_name='个人简介', blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(verbose_name='昵称', blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='qq_id',
            field=models.CharField(verbose_name='QQ账号', blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='wechat_id',
            field=models.CharField(verbose_name='微信账号', blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weibo_id',
            field=models.CharField(verbose_name='微博账号', blank=True, max_length=50, null=True),
        ),
    ]
