from django.conf.urls import url, include
from . import views

def test(req):
    print "---------> APP Urls"

urlpatterns = [
    url(r'^register', views.register),
    url(r'^signin', views.sign_in),
    url(r'^signout', views.process_out),
    url(r'^process_reg', views.process_reg),
    url(r'^process_in', views.process_in)
] 