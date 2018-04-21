from django.conf.urls import url
from apps.blog_article import views

urlpatterns = [
    url(r'^([0-9].+)$', views.article_id)
]
