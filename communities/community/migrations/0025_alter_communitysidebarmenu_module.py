# Generated by Django 4.2.4 on 2024-04-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0024_alter_communitysidebarmenu_module_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communitysidebarmenu",
            name="module",
            field=models.TextField(
                choices=[
                    ("grappelli", "grappelli"),
                    ("django.contrib.admin", "django.contrib.admin"),
                    ("django.contrib.auth", "django.contrib.auth"),
                    ("django.contrib.contenttypes", "django.contrib.contenttypes"),
                    ("django.contrib.sessions", "django.contrib.sessions"),
                    ("django.contrib.messages", "django.contrib.messages"),
                    ("django.contrib.staticfiles", "django.contrib.staticfiles"),
                    ("django.contrib.humanize", "django.contrib.humanize"),
                    ("django_bootstrap5", "django_bootstrap5"),
                    ("jsignature", "jsignature"),
                    ("django_registration", "django_registration"),
                    ("storages", "storages"),
                    ("martor", "martor"),
                    ("mathfilters", "mathfilters"),
                    ("phonenumber_field", "phonenumber_field"),
                    ("colorful", "colorful"),
                    ("communities.preferences", "communities.preferences"),
                    ("content_manager.emoji", "content_manager.emoji"),
                    ("content_manager.categories", "content_manager.categories"),
                    ("communities.notifications", "communities.notifications"),
                    ("dashboard", "dashboard"),
                    ("core.dynapages", "core.dynapages"),
                    ("communities.profiles", "communities.profiles"),
                    ("roleplaying.comms", "roleplaying.comms"),
                    ("communities.stream", "communities.stream"),
                    ("communities.group", "communities.group"),
                    ("content_manager.keywords", "content_manager.keywords"),
                    ("communities.community", "communities.community"),
                    ("core.plyscript", "core.plyscript"),
                    ("core.authentication", "core.authentication"),
                    ("core.authentication.ui", "core.authentication.ui"),
                    ("media.gallery.core", "media.gallery.core"),
                    ("media.gallery.images", "media.gallery.images"),
                    ("core.metrics", "core.metrics"),
                    ("roleplaying.stats", "roleplaying.stats"),
                    ("roleplaying.combat", "roleplaying.combat"),
                    ("roleplaying.skills", "roleplaying.skills"),
                    ("roleplaying.equipment", "roleplaying.equipment"),
                    ("roleplaying.spells", "roleplaying.spells"),
                    ("roleplaying.items", "roleplaying.items"),
                    ("core.forge", "core.forge"),
                    ("content_manager.almanac", "content_manager.almanac"),
                    ("core.plyui", "core.plyui"),
                    ("roleplaying.exp", "roleplaying.exp"),
                    ("roleplaying.SLHUD", "roleplaying.SLHUD"),
                    ("roleplaying.plydice", "roleplaying.plydice"),
                    ("ply", "ply"),
                    (
                        "core.plyui.themes.default_theme",
                        "core.plyui.themes.default_theme",
                    ),
                ],
                max_length=200,
                verbose_name="Module",
            ),
        ),
    ]
