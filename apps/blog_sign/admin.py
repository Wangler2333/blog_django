from django.contrib import admin
from apps.blog_sign import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.UserInfo)
