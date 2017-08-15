from django.conf.urls import url
from . import views

def test(req):
    print "--------> App routing test"

urlpatterns = [
    url(r'^$', views.view_all),
    url(r'(?P<requested_id>\d+$)', views.view_single),
    url(r'(?P<requested_id>\d+)/edit$', views.create_edit),
    url(r'^/new', views.create_edit),
    url(r'/save$', views.save),
    url(r'(?P<requested_id>\d+)/delete$', views.destroy),
]
