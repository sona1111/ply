# Generated by Django 4.0.2 on 2022-05-08 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend1',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='friend2',
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
