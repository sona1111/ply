# Generated by Django 4.0.4 on 2022-08-10 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynapages', '0011_templates_app'),
        ('profiles', '0004_profile_mentions_profile_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Dashboard Dynapage Node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='dynapages.page'),
        ),
    ]