from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'login$', views.login),
    url(r'register$', views.register),
    url(r'register$', views.success),
]
