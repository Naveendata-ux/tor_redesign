# Generated by Django 2.2.5 on 2020-06-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20200630_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptionplan',
            old_name='Account_type',
            new_name='account_type',
        ),
    ]
