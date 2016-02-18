from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.homemade_login, name='login'),
]