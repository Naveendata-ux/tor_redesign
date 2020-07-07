"""Admin views for the Flexible Subscriptions app."""
from django.contrib import admin

from subscriptions import models
from subscriptions.conf import SETTINGS
from .models import *

admin.site.register(PlanCost)
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(PlanTag)
admin.site.register(PlanList)
admin.site.register(SubscriptionTransaction)
admin.site.register(PlanListDetail)


