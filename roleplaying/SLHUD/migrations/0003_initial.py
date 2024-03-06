# Generated by Django 4.2.4 on 2023-08-15 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('SLHUD', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slagent',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Active Character Profile'),
        ),
        migrations.AddIndex(
            model_name='slparcelagent',
            index=models.Index(fields=['uuid'], name='roleplaying_uuid_26332d_idx'),
        ),
    ]