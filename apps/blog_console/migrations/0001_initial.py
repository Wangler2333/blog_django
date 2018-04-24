# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogHtml',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('article', models.TextField(verbose_name='文章')),
            ],
            options={
                'verbose_name': 'Html列表',
                'verbose_name_plural': 'Html列表',
                'db_table': 'blog_html',
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='描述', max_length=30)),
                ('image', models.ImageField(upload_to='image', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图片列表',
                'verbose_name_plural': '图片列表',
                'db_table': 'blog_image',
            },
        ),
        migrations.CreateModel(
            name='BlogMarkdown',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('article', models.TextField(verbose_name='文章')),
            ],
            options={
                'verbose_name': 'Markdown列表',
                'verbose_name_plural': 'Markdown列表',
                'db_table': 'blog_markdown',
            },
        ),
    ]
