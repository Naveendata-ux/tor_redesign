from django.contrib.auth.models import User
import django_filters
from core.models import Ad

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Ad
        fields = ['Ad_title', 'offer_price', ]
