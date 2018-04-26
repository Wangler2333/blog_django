from django.conf.urls import url
from apps.blog_index import views

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+$)', views.user_index),
    url(r'^$', views.index, name='index'),
]
