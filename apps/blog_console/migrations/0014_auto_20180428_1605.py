# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0013_blogimagethumbs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogarticleid',
            options={'verbose_name_plural': '文章id分配暂存', 'verbose_name': '文章id分配暂存'},
        ),
        migrations.AlterModelOptions(
            name='blogimagethumbs',
            options={'verbose_name_plural': '缩略图列表', 'verbose_name': '缩略图列表'},
        ),
        migrations.AlterModelTable(
            name='blogarticleid',
            table='blog_article_id',
        ),
        migrations.AlterModelTable(
            name='blogimagethumbs',
            table='blog_image_thumbs',
        ),
    ]
