# Generated by Django 2.2.5 on 2020-06-30 06:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanCost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, help_text='slug to reference these cost details', max_length=128, null=True, unique=True)),
                ('recurrence_period', models.PositiveSmallIntegerField(default=1, help_text='how often the plan is billed (per recurrence unit)', validators=[django.core.validators.MinValueValidator(1)])),
                ('recurrence_unit', models.CharField(choices=[('0', 'once'), ('1', 'second'), ('2', 'minute'), ('3', 'hour'), ('4', 'day'), ('5', 'week'), ('6', 'month'), ('7', 'year')], default='6', max_length=1)),
                ('cost', models.DecimalField(blank=True, decimal_places=4, help_text='the cost per recurrence of the plan', max_digits=19, null=True)),
            ],
            options={
                'ordering': ('recurrence_unit', 'recurrence_period', 'cost'),
            },
        ),
        migrations.CreateModel(
            name='PlanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, help_text='title to display on the subscription plan list page', null=True)),
                ('slug', models.SlugField(blank=True, help_text='slug to reference the subscription plan list', max_length=128, null=True, unique=True)),
                ('subtitle', models.TextField(blank=True, help_text='subtitle to display on the subscription plan list page', null=True)),
                ('header', models.TextField(blank=True, help_text='header text to display on the subscription plan list page', null=True)),
                ('footer', models.TextField(blank=True, help_text='header text to display on the subscription plan list page', null=True)),
                ('active', models.BooleanField(default=True, help_text='whether this plan list is active or not.')),
            ],
        ),
        migrations.CreateModel(
            name='PlanTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='the tag name', max_length=64, unique=True)),
            ],
            options={
                'ordering': ('tag',),
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_billing_start', models.DateTimeField(blank=True, help_text='the date to start billing this subscription', null=True, verbose_name='billing start date')),
                ('date_billing_end', models.DateTimeField(blank=True, help_text='the date to finish billing this subscription', null=True, verbose_name='billing start end')),
                ('date_billing_last', models.DateTimeField(blank=True, help_text='the last date this plan was billed', null=True, verbose_name='last billing date')),
                ('date_billing_next', models.DateTimeField(blank=True, help_text='the next date billing is due', null=True, verbose_name='next start date')),
                ('active', models.BooleanField(default=True, help_text='whether this subscription is active or not')),
                ('cancelled', models.BooleanField(default=False, help_text='whether this subscription is cancelled or not')),
                ('subscription', models.ForeignKey(help_text='the plan costs and billing frequency for this user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscriptions.PlanCost')),
                ('user', models.ForeignKey(help_text='the user this subscription applies to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user', 'date_billing_start'),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transaction', models.DateTimeField(help_text='the datetime the transaction was billed', verbose_name='transaction date')),
                ('amount', models.DecimalField(blank=True, decimal_places=4, help_text='how much was billed for the user', max_digits=19, null=True)),
                ('subscription', models.ForeignKey(help_text='the plan costs that were billed', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='subscriptions.PlanCost')),
                ('user', models.ForeignKey(help_text='the user that this subscription was billed for', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription_transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_transaction', 'user'),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(help_text='the name of the subscription plan', max_length=128)),
                ('slug', models.SlugField(blank=True, help_text='slug to reference the subscription plan', max_length=128, null=True, unique=True)),
                ('plan_description', models.CharField(blank=True, help_text='a description of the subscription plan', max_length=512, null=True)),
                ('grace_period', models.PositiveIntegerField(default=0, help_text='how many days after the subscription ends before the subscription expires')),
                ('post_count', models.PositiveIntegerField(default=0, help_text='how many posts for these subscription')),
                ('days_count', models.PositiveIntegerField(default=0, help_text='how many days for subscription')),
                ('group', models.ForeignKey(blank=True, help_text='the Django auth group for this plan', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plans', to='auth.Group')),
                ('tags', models.ManyToManyField(blank=True, help_text='any tags associated with this plan', related_name='plans', to='subscriptions.PlanTag')),
            ],
            options={
                'ordering': ('plan_name', 'post_count'),
                'permissions': (('subscriptions', 'Can interact with subscription details'),),
            },
        ),
        migrations.CreateModel(
            name='PlanListDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_content', models.TextField(blank=True, help_text='HTML content to display for plan', null=True)),
                ('subscribe_button_text', models.CharField(blank=True, default='Subscribe', max_length=128, null=True)),
                ('order', models.PositiveIntegerField(default=1, help_text='Order to display plan in (lower numbers displayed first)')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_list_details', to='subscriptions.SubscriptionPlan')),
                ('plan_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_list_details', to='subscriptions.PlanList')),
            ],
        ),
        migrations.AddField(
            model_name='plancost',
            name='plan',
            field=models.ForeignKey(help_text='the subscription plan for these cost details', on_delete=django.db.models.deletion.CASCADE, related_name='costs', to='subscriptions.SubscriptionPlan'),
        ),
    ]
