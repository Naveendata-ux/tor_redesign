# Generated by Django 3.0.5 on 2020-06-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200615_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Account_Type',
        ),
        migrations.AddField(
            model_name='user',
            name='Account_type',
            field=models.CharField(choices=[('Business', 'Business'), ('Personal', 'Personal')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
