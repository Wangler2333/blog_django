# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_console', '0002_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='article',
            field=models.ForeignKey(null=True, to='blog_console.BlogMarkdown', blank=True, verbose_name='所属文章'),
        ),
    ]
