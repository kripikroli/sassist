# Generated by Django 3.2.2 on 2021-05-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partneruser',
            name='is_added_by_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientuser',
            name='is_added_by_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='staffuser',
            name='is_added_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
