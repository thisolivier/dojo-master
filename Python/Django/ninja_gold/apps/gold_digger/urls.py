from django.conf.urls import url
from . import views

def test(req):
    print "-------> We have reached the gold_digger"

urlpatterns = [
    url(r'^$', views.render_world),
    url(r'reset$', views.reset),
    url(r'goldme$', views.dig4gold),
]
