# Generated by Django 3.0.4 on 2020-04-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_actualvitals'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
