from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.upload_form),
    url(r'process_upload$', views.process_upload),
    url(r'reset$', views.reset),
]
