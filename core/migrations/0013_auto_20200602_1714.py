# Generated by Django 3.0.5 on 2020-06-02 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_ad_tyre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='tyre',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Tyres'),
        ),
    ]
