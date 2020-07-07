"""paths for the Flexible Subscriptions app."""
# pylint: disable=line-too-long
import importlib

from django.urls import path

from subscriptions import views
from subscriptions.conf import SETTINGS


# Retrieve the proper subscribe view
SubscribeView = getattr(  # pylint: disable=invalid-name
    importlib.import_module(SETTINGS['subscribe_view']['module']),
    SETTINGS['subscribe_view']['class']
)


urlpatterns = [
    path(
        'subscribe/',
        views.SubscribeList.as_view(),
        name='dfs_subscribe_list',
    ),
    path(
        'subscribe/add/',
        SubscribeView.as_view(),
        name='dfs_subscribe_add',
    ),
    path(
        'subscribe/thank-you/<uuid:transaction_id>/',
        views.SubscribeThankYouView.as_view(),
        name='dfs_subscribe_thank_you',
    ),
    path(
        'subscribe/cancel/<uuid:subscription_id>/',
        views.SubscribeCancelView.as_view(),
        name='dfs_subscribe_cancel',
    ),
    path(
        'subscriptions/',
        views.SubscribeUserList.as_view(),
        name='dfs_subscribe_user_list',
    ),
    path(
        'dfs/tags/',
        views.TagListView.as_view(),
        name='dfs_tag_list',
    ),
    path(
        'dfs/tags/create/',
        views.TagCreateView.as_view(),
        name='dfs_tag_create',
    ),
    path(
        'dfs/tags/<int:tag_id>/',
        views.TagUpdateView.as_view(),
        name='dfs_tag_update',
    ),
    path(
        'dfs/tags/<int:tag_id>/delete/',
        views.TagDeleteView.as_view(),
        name='dfs_tag_delete',
    ),
    path(
        'dfs/plans/',
        views.PlanListView.as_view(),
        name='dfs_plan_list',
    ),
    path(
        'dfs/plans/create/',
        views.PlanCreateView.as_view(),
        name='dfs_plan_create',
    ),
    path(
        'dfs/plans/<uuid:plan_id>/',
        views.PlanUpdateView.as_view(),
        name='dfs_plan_update',
    ),
    path(
        'dfs/plans/<uuid:plan_id>/delete/',
        views.PlanDeleteView.as_view(),
        name='dfs_plan_delete',
    ),
    path(
        'dfs/plan-lists/',
        views.PlanListListView.as_view(),
        name='dfs_plan_list_list',
    ),
    path(
        'dfs/plan-lists/create/',
        views.PlanListCreateView.as_view(),
        name='dfs_plan_list_create',
    ),
    path(
        'dfs/plan-lists/<int:plan_list_id>/',
        views.PlanListUpdateView.as_view(),
        name='dfs_plan_list_update',
    ),
    path(
        'dfs/plan-lists/<int:plan_list_id>/delete/',
        views.PlanListDeleteView.as_view(),
        name='dfs_plan_list_delete',
    ),
    path(
        'dfs/plan-lists/<int:plan_list_id>/details/',
        views.PlanListDetailListView.as_view(),
        name='dfs_plan_list_detail_list',
    ),
    path(
        'dfs/plan-lists/<int:plan_list_id>/details/create/',
        views.PlanListDetailCreateView.as_view(),
        name='dfs_plan_list_detail_create',
    ),
    path(
        'dfs/plan-lists/<int:plan_list_id>/details/<int:plan_list_detail_id>/',
        views.PlanListDetailUpdateView.as_view(),
        name='dfs_plan_list_detail_update',
    ),
    path(
        'dfs/plan-lists/<int:plan_list_id>/details/<int:plan_list_detail_id>/delete/',
        views.PlanListDetailDeleteView.as_view(),
        name='dfs_plan_list_detail_delete',
    ),
    path(
        'dfs/subscriptions/',
        views.SubscriptionListView.as_view(),
        name='dfs_subscription_list',
    ),
    path(
        'dfs/subscriptions/create/',
        views.SubscriptionCreateView.as_view(),
        name='dfs_subscription_create',
    ),
    path(
        'dfs/subscriptions/<uuid:subscription_id>/',
        views.SubscriptionUpdateView.as_view(),
        name='dfs_subscription_update',
    ),
    path(
        'dfs/subscriptions/<uuid:subscription_id>/delete/',
        views.SubscriptionDeleteView.as_view(),
        name='dfs_subscription_delete',
    ),
    path(
        'dfs/transactions/',
        views.TransactionListView.as_view(),
        name='dfs_transaction_list',
    ),
    path(
        'dfs/transactions/<uuid:transaction_id>/',
        views.TransactionDetailView.as_view(),
        name='dfs_transaction_detail',
    ),
    path(
        'dfs/',
        views.DashboardView.as_view(),
        name='dfs_dashboard',
    ),
]
