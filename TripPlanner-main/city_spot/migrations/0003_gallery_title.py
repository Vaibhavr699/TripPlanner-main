# Generated by Django 4.2.5 on 2023-09-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_spot', '0002_spot_spot_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='photo-site', max_length=200),
        ),
    ]
