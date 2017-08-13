from django.conf.urls import url
from . import views

def test(req):
    print "------> Store_app routing reached"

urlpatterns = [
    url(r'^$', views.test),
    url(r'buy$', views.process),
    url(r'purchase$', views.complete),
    url(r'reset$', views.reset),

]