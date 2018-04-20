from django.conf.urls import url
from apps.blog_index import views

urlpatterns = [
    url(r'^(?P<user_id>.*)', views.index, name='index')
]
