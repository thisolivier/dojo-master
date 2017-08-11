from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'users$', views.users_all),
    url(r'new$', views.users_new),
    url(r'(?P<action>register|login)', views.users_entry)
]