# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0004_blogarticleid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghtml',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
    ]
