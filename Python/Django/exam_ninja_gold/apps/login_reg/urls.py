from django.conf.urls import url
from . import views

def test(req):
    print "--------> Login routing reached"

urlpatterns = [
    url(r'^$', views.display_log_reg),
    url(r'in$', views.process_log)
]
