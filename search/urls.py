from django.conf.urls import url
from django.contrib import admin
from .views import (searchposts)
from . import views

urlpatterns = [
     url(r'^$', searchposts, name='searchposts'),
     url(r'^$', views.index, name='index'),

]
