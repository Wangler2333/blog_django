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
from dj_blog import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # 添加static文件夹和media文件夹的路径
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # 设置各个APP的url路径
    url(r'^$', include('apps.blog_index.urls')),
    url(r'^index/', include('apps.blog_index.urls', namespace='index')),
    url(r'^sign/', include('apps.blog_sign.urls', namespace='sign')),
    url(r'^article/', include('apps.blog_article.urls', namespace='article')),
    url(r'^console/', include('apps.blog_console.urls', namespace='console')),
]

# urlpatterns += static(settings.MEDIA_DIR, document_root=settings.MEDIA_ROOT)  # 另一种添加media的路径的方法
