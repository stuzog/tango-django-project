from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.rangoindex, name='rangoindex'),
    url(r'^about/', views.rangoabout, name='rangoabout'),
    url(r'^contact/', views.rangocontact, name='rangocontact'),
    url(r'^files/', views.rangofiles, name='rangofiles'),
    url(r'^links/', views.rangolinks, name='rangolinks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
