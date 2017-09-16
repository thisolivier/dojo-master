from django.conf.urls import url, include
from . import views

def test(req):
    print "---------> APP Urls"

urlpatterns = [
    url(r'^$', views.main_dash),
    url(r'^admin', views.main_dash),
    url(r'^edit/(?P<target>\d+)', views.edit_user),
    url(r'^edit', views.edit_user),
    url(r'^save/(?P<target>.+)', views.save_changes),
    url(r'^remove/(?P<target>.+)', views.delete_user)
]