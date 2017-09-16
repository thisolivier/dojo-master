from django.conf.urls import url
from . import views

def test(req):
    print "--------> Game routing reached"

urlpatterns = [
    url(r'^$', views.display_game),
    url(r'fight/(?P<opponent>.+)$', views.proccess_fight)
]