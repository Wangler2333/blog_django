# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0006_auto_20180427_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimage',
            name='is_show',
            field=models.BooleanField(verbose_name='是否展示', default=False),
        ),
    ]
