from django.conf.urls import url
from apps.blog_index import views

urlpatterns = [
    url(r'^img/([0-9]+)', views.img, name="img"),
    url(r'^([0-9]+)', views.user_index),
    url(r'^$', views.index, name='index'),
]
