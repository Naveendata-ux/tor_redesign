from django.urls import path
from django.conf.urls import url

from .views import *
from core import views

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('listings', ListingListView.as_view(), name="listings"),
    url(r'^about/', about_page_view, name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^help&support/', helpsupport_page_view, name='helpsupport'),
    url(r'^FAQs/', faqs_page_view, name='faqs'),
    url(r'^privacy-policy/', privacy_policy_view, name='privacypolicy'),
    url(r'^terms_of_service/', terms_of_service_view, name='termsofservice'),
]
