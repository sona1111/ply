# Generated by Django 4.2.4 on 2023-10-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_community_icon_community_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='tagline',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Tagline'),
        ),
    ]