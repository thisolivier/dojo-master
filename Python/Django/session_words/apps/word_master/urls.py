from django.conf.urls import url
from . import views

def test2(req):
    print "--------> Hello Elvis!"
    return

urlpatterns = [
    url(r'^$', views.root),
    url(r'reset/?$', views.reset),
    url(r'add/?$', views.process),
]