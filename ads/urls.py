from django.urls import path
from django.conf.urls import url

from .views import *
from . import views

app_name = "ads"

urlpatterns = [
    path('<int:ad_id>', AdDetailsView.as_view(), name="ad.details"),
    path('create', AdCreateView.as_view(), name="crate.ad"),
    url(
        r"^add/select-type/$", views.ad_select_type, name="ad-add-select-type"
    ),
    path('<int:ad_id>/update', AdUpdateView.as_view(), name="update.ad"),
    path('<int:ad_id>/delete', AdDeleteView.as_view(), name="delete.ad"),
    url(r'^postad/tyre/$', views.tyresad, name='tyresad'),
    url(r'^postad/wheels/$', views.wheelsad, name='wheelsad'),
    url(r'^postad/category/$', views.post_ad_view, name='category'),
]
