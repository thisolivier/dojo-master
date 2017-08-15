from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_all),
    url(r'new$', views.add),
    url(r'(?P<course_id>\d+)/destroy/$', views.confirm),
    url(r'(?P<course_id>\d+)/destroy/confirm$', views.destroy)
]
