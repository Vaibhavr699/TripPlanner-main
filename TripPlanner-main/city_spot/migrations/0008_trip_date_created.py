# Generated by Django 4.2.5 on 2023-09-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_spot', '0007_alter_profile_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]