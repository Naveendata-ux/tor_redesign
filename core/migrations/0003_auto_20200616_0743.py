# Generated by Django 3.0.5 on 2020-06-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200616_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(upload_to='ads_images', verbose_name='image'),
        ),
    ]