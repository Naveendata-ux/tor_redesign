# Generated by Django 2.2.5 on 2020-06-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20200630_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='cost',
            field=models.PositiveIntegerField(blank=True, help_text='the cost per recurrence of the plan', null=True),
        ),
    ]
