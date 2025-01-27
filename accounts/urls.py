from django.urls import path
from django.conf.urls import url

from .views import *
from . import views
app_name = 'accounts'

urlpatterns = [
   # path('register', RegisterView.as_view(), name='register'),
    path('register', views.signup, name='register'),
    #path('login', views.user_login, name='login'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('insurance/', InsuranceInfoView.as_view(), name='insurance-info'),
]
