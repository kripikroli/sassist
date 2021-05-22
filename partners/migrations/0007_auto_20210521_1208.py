# Generated by Django 3.2.1 on 2021-05-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0006_alter_partnerlicense_is_compact'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnereducationmedia',
            name='media_format',
            field=models.IntegerField(choices=[(1, 'JPG'), (2, 'PNG'), (3, 'PDF')], default=1),
        ),
        migrations.AlterField(
            model_name='partnereducationmedia',
            name='media_content',
            field=models.FileField(blank=True, upload_to='education_files'),
        ),
    ]
