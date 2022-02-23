# Generated by Django 4.0.2 on 2022-02-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0032_profilepermission_profile_profilepermission_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='SHIELD',
            field=models.TextField(default=10, verbose_name='Current SHIELD'),
        ),
        migrations.AddField(
            model_name='profile',
            name='STUN',
            field=models.TextField(default=10, verbose_name='Current STUN'),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_SHIELD',
            field=models.TextField(default=6, verbose_name='Max SHIELD'),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_STUN',
            field=models.TextField(default=6, verbose_name='Max STUN'),
        ),
    ]