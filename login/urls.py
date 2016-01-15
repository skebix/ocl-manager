from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
    url(r'^services/', views.ServicesView.as_view(), name='services')
]