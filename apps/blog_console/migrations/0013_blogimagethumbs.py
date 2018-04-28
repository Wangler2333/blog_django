# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0012_remove_blogimage_image_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImageThumbs',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image_thumb', models.ImageField(upload_to='image', verbose_name='缩略图')),
                ('image', models.OneToOneField(verbose_name='原图', to='blog_console.BlogImage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
