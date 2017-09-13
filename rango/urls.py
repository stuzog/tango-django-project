from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.rangoIndex, name='rangoIndex'),
    url(r'^about/', views.rangoAbout, name='rangoAbout'),
    url(r'^contact/', views.rangoContact, name='rangoContact'),
    url(r'^files/', views.rangoFiles, name='rangoFiles'),
    url(r'^links/', views.rangoLinks, name='rangoLinks'),
]

