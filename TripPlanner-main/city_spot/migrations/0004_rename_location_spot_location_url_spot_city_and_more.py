# Generated by Django 4.2.5 on 2023-09-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_spot', '0003_gallery_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='location',
            new_name='location_url',
        ),
        migrations.AddField(
            model_name='spot',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='spot',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]