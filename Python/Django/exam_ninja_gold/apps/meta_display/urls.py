from django.conf.urls import url
from . import views

def test(req):
    print "--------> Meta routing reached"

urlpatterns = [
    url(r'^$', views.display_home),
    url(r'viewall$', views.display_all),
    url(r'user/(?P<user_id>.+)$', views.inspect_single)
]