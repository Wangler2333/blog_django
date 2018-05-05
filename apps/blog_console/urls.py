from django.conf.urls import url
from apps.blog_console import views

urlpatterns = [
    url(r'^user$', views.UserView.as_view(), name='user'),
    url(r'^gallery$', views.GalleryView.as_view(), name='gallery'),
    url(r'^table$', views.TableView.as_view(), name='table'),
    url(r'^form$', views.FormView.as_view(), name='form'),
    url(r'^upload_image$', views.upload_image, name='upload_image')
]
