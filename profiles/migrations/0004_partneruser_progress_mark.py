# Generated by Django 3.2.1 on 2021-05-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_partneruser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='partneruser',
            name='progress_mark',
            field=models.IntegerField(default=20),
        ),
    ]