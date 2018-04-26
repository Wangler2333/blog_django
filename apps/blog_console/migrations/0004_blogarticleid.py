# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_console', '0003_auto_20180426_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticleId',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('user', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
