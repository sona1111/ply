# Generated by Django 4.0.2 on 2022-05-08 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_friend_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='community',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community'),
            preserve_default=False,
        ),
    ]