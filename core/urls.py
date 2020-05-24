from django.urls import path
from django.conf.urls import url

from .views import *

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('listings', ListingListView.as_view(), name="listings"),
    url(r'^about/', about_page_view, name='about'),
    url(r'^contact/', contact_page_view, name='contact'),
    url(r'^help&support/', helpsupport_page_view, name='helpsupport'),
    url(r'^FAQs/', faqs_page_view, name='faqs'),
]
