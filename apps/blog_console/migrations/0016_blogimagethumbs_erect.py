# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0015_auto_20180430_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimagethumbs',
            name='erect',
            field=models.BooleanField(verbose_name='是否竖向', default=False),
            preserve_default=False,
        ),
    ]
