# Generated by Django 4.0.2 on 2022-02-24 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0033_profile_shield_profile_stun_profile_max_shield_and_more'),
        ('community', '0014_community_action_call_cover_community_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='vhost',
            name='restricted',
            field=models.BooleanField(default=False, verbose_name='Restricted Joining FLAG'),
        ),
        migrations.CreateModel(
            name='CommunityAdmins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined', models.DateTimeField(verbose_name='Joined')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='User')),
            ],
        ),
    ]