# Generated by Django 2.2.5 on 2020-07-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20200630_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='active',
            field=models.BooleanField(default=True, help_text='whether this plan list is active or not.'),
        ),
    ]
