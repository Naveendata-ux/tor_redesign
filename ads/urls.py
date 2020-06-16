from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

app_name = "ads"

urlpatterns = [
    path('<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    url('create', AdCreateView.as_view(), name="crate.ad"),
    path('<int:ad_id>/update', AdUpdateView.as_view(), name="update.ad"),
    path('<int:ad_id>/delete', AdDeleteView.as_view(), name="delete.ad"),
    url('favourite_list/$', views.ad_favourite_list, name='favourite_ads'),
    
    
]
