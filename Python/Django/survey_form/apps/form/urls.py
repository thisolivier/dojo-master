from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'process$', views.process),
    url(r'result$', views.result),
]