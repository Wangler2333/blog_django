# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0010_auto_20180428_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='image_thumbnail',
            field=models.ImageField(upload_to='image', verbose_name='缩略图'),
        ),
    ]
