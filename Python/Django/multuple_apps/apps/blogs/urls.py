from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^\/?$', views.blog_root),
    url(r'new\/?$', views.blog_new),
    url(r'create\/?$', views.blog_create),
    url(r'(?P<number>\d+$)', views.blog_num),
    url(r'(?P<number>\d+)\/(?P<action>edit|delete)', views.blog_modify),
]


