from django.conf.urls import url
from apps.blog_index import views

urlpatterns = [
    url(r'^index$', views.index, name='index')
]
