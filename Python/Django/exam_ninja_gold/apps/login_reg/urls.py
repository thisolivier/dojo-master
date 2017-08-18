from django.conf.urls import url
from . import views

def test(req):
    print "--------> Login routing reached"

urlpatterns = [
    url(r'^$', views.display_log_reg),
    url(r'process$', views.process_log),
    url(r'out$', views.process_logout)
]
