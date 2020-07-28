from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

app_name = "ads"

urlpatterns = [
    path('<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    url('tires', AdCreateView.as_view(), name="crate.ad"),
    url('wheels', AdCreateViewWheels.as_view(), name="wheels.ad"),
    url('services', AdCreateViewServices.as_view(), name="service.ad"),
    path('<int:ad_id>/update', AdUpdateView.as_view(), name="update.ad"),
    path('<int:ad_id>/delete', AdDeleteView.as_view(), name="delete.ad"),
    url('favourite_list/$', views.ad_favourite_list, name='favourite_ads'),
    
    url(r'^filter$', views.filter, name='filter'),
    url(r'^filter_w$', views.filter_wheels, name='filter.wheels'),
    url(r'^filter_s$', views.filter_services, name='filter.services'),
    url(r'^search$', views.search, name='search'),
    
    
]
