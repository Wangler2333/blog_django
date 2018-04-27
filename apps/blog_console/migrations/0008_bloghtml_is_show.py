# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0007_blogimage_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloghtml',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否发布'),
        ),
    ]
