# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0011_auto_20180428_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogimage',
            name='image_thumbnail',
        ),
    ]
