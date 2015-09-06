from django.conf.urls import url 

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^new_url/$', views.new_url, name='new_url'),
] 