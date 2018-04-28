# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0009_blogimage_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='image_thumbnail',
            field=models.CharField(max_length=100, verbose_name='缩略图路径'),
        ),
    ]
