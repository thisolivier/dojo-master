from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.display_portal),
    url(r'^process', views.process_login),
]
