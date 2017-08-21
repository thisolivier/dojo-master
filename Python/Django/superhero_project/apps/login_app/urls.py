from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.portal),
    url(r'^register', views.register),
    url(r'^signin', views.signin),
]
