from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'register$', views.register),
    url(r'login$', views.login)
]
