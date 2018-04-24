# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_console', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmarkdown',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogimage',
            name='article',
            field=models.ForeignKey(null=True, blank=True, verbose_name='所属文章', to='blog_console.BlogMarkdown'),
        ),
        migrations.AddField(
            model_name='blogimage',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloghtml',
            name='markdown',
            field=models.OneToOneField(verbose_name='markdown文章ID', to='blog_console.BlogMarkdown'),
        ),
        migrations.AddField(
            model_name='bloghtml',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL),
        ),
    ]
