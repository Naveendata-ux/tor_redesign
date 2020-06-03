# Generated by Django 3.0.5 on 2020-05-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_student', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('is_senior_citizen', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('is_ersm', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('student', models.CharField(blank=True, max_length=25)),
                ('senior_age', models.SmallIntegerField()),
                ('student_id', models.ImageField(upload_to='student_uploads', verbose_name='Student id')),
                ('senior_citizen_id', models.ImageField(upload_to='senior_uploads', verbose_name='Senior id')),
                ('ersm_yes_questions', models.CharField(max_length=125)),
                ('ersm_no_questions', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, verbose_name='Contact number'),
        ),
    ]
