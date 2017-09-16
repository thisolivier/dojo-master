from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^like_hero/(?P<target>.+)', views.like_hero),
    url(r'^hate_hero/(?P<target>.+)', views.hate_hero),
    url(r'^$', views.show_all),
]
