from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gen_root),
    url(r'reset$', views.gen_reset),
]