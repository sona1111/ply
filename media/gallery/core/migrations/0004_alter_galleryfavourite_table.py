# Generated by Django 4.2.4 on 2023-08-15 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_galleryfavourite_galleryfavourite_unique_favourite'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='galleryfavourite',
            table='media_gallery_core_favourite',
        ),
    ]
