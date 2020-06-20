from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from search.urls import urlpatterns as search_urls
from django_private_chat import urls as django_private_chat_urls
import subscriptions
from django.contrib.auth import views as auth_views
from .views import user_dialogs

urlpatterns = [
    path('api/', include('core.api.urls')),
    path('torca/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    url('^', include('django.contrib.auth.urls')),
    path('ads/', include('ads.urls')),
    path('users/', include('users.urls')),
    path('messages/', user_dialogs, name="user_dialogs_url"),
    path('', include('core.urls')),
    path('categories', include('category.urls')),
    url(r"^search/", include((search_urls, "search"), namespace="search")),
    url('', include('django_private_chat.urls')),
   # url(r'^messages/', include('django_messages.urls')),
    url(r'^subscriptions/', include('subscriptions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
