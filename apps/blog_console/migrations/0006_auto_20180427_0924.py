# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0005_auto_20180427_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimage',
            name='is_head',
            field=models.BooleanField(default=False, verbose_name='是否为头像'),
        ),
        migrations.AlterField(
            model_name='blogimage',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blogmarkdown',
            name='article',
            field=models.TextField(verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='blogmarkdown',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
    ]
