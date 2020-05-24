from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.

from .models import *

admin.site.register(User)
class MyAdminSite(AdminSite):
    site_header = 'Tires On Rent'

admin_site = MyAdminSite(name='torca')

