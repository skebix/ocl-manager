__author__ = 'skebix'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crear-store$', views.create_store, name='create_store'),
    url(r'^$', views.index, name='index')
]