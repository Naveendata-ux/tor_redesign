from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from search.urls import urlpatterns as search_urls
from django_private_chat import urls as django_private_chat_urls
import subscriptions
from django.contrib.auth import views as auth_views
from .views import user_dialogs, checkout,create_sub,complete
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('api/', include('core.api.urls')),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path('accounts/', include('allauth.urls')),
    path('torca/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    url('^', include('django.contrib.auth.urls')),
    path('ads/', include('ads.urls')),
    path('users/', include('users.urls')),
    path('dialogs/', user_dialogs, name="user_dialogs_url"),
    path('', include('core.urls')),
    path('categories', include('category.urls')),
    url(r"^search/", include((search_urls, "search"), namespace="search")),
    url('', include('django_private_chat.urls')),
   # url(r'^messages/', include('django_messages.urls')),
    url(r'^subscriptions/', include('subscriptions.urls')),
    path('checkout/', checkout, name='checkout'),
    path("create-sub", create_sub, name="create sub"), #add
	path("complete", complete, name="complete"), #add
	path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
