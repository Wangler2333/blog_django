# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0008_bloghtml_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimage',
            name='image_thumbnail',
            field=models.ImageField(default=1, upload_to='image', verbose_name='缩略图'),
            preserve_default=False,
        ),
    ]
