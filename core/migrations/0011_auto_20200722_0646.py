# Generated by Django 2.2.5 on 2020-07-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200722_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='Seasonality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='Wheels_Brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='service_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='specials',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='wheel_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='wheel_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
