"""dj_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from dj_blog import settings

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  # 设置各个APP的url路径
                  url(r'^index/', include('apps.blog_index.urls', namespace='index')),
                  url(r'^sign/', include('apps.blog_sign.urls', namespace='sign')),
                  url(r'^article/', include('apps.blog_article.urls', namespace='article')),
                  url(r'^console/', include('apps.blog_console.urls', namespace='console')),
              ] + static(settings.MEDIA_DIR, document_root=settings.MEDIA_DIR)  # 添加media的url路径
