from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.surveys_root),
 url(r'new$', views.surveys_new),
]