from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^power', views.power_form),
    url(r'^add_power', views.add_power),
    url(r'^hero', views.hero_form),
    url(r'^add_hero', views.add_hero),
    url(r'^view_hero/(?P<target>\d+)', views.view_hero),
    url(r'^save_hero', views.save_hero),
]
