from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'^/register', views.register_page),
    url(r'^/register/do', views.register),
    url(r'^/do', views.login)
]
