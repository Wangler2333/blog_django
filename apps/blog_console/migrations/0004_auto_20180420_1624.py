# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_console', '0003_auto_20180420_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('article', models.TextField(verbose_name='文章')),
            ],
            options={
                'verbose_name_plural': 'Html列表',
                'verbose_name': 'Html列表',
                'db_table': 'blog_html',
            },
        ),
        migrations.AlterField(
            model_name='blogmarkdown',
            name='article',
            field=models.TextField(verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='bloghtml',
            name='article_id',
            field=models.OneToOneField(verbose_name='markdown文章ID', to='blog_console.BlogMarkdown'),
        ),
        migrations.AddField(
            model_name='bloghtml',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL),
        ),
    ]
