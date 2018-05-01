# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0014_auto_20180428_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimagethumbs',
            name='height',
            field=models.IntegerField(default=1, verbose_name='高度'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogimagethumbs',
            name='width',
            field=models.IntegerField(default=1, verbose_name='宽度'),
            preserve_default=False,
        ),
    ]
