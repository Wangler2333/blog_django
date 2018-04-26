# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0002_auto_20180422_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghtml',
            name='title',
            field=models.CharField(verbose_name='标题', blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blogimage',
            name='title',
            field=models.CharField(verbose_name='描述', blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blogmarkdown',
            name='article',
            field=models.TextField(blank=True, verbose_name='文章', null=True),
        ),
        migrations.AlterField(
            model_name='blogmarkdown',
            name='title',
            field=models.CharField(verbose_name='标题', blank=True, max_length=30, null=True),
        ),
    ]
