from django.urls import path
from django.conf.urls import url

from .views import *
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    url('profile', views.Profileupdate, name="profile"),
]
