# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0004_auto_20180420_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloghtml',
            old_name='article_id',
            new_name='markdown',
        ),
    ]
