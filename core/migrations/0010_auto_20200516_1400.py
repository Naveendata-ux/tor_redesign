# Generated by Django 3.0.5 on 2020-05-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200414_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='make',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='rent_type',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
