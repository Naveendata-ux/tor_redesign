# Generated by Django 2.2.5 on 2020-07-01 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0009_planlistdetail_plan_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planlistdetail',
            name='plan_cost',
        ),
        migrations.AddField(
            model_name='planlist',
            name='plan_cost',
            field=models.ForeignKey(help_text='the plan costs that were billed', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_cost', to='subscriptions.PlanCost'),
        ),
    ]
