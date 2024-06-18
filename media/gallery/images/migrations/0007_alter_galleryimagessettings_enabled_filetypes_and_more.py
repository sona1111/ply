# Generated by Django 5.0.1 on 2024-05-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0006_galleryimagessettings_enable_icc_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimagessettings",
            name="enabled_filetypes",
            field=models.ManyToManyField(
                help_text="Select which File types are allowed in this Gallery.",
                to="images.galleryimagesfiletypes",
                verbose_name="Enabled Input Filetypes",
            ),
        ),
        migrations.AlterField(
            model_name="galleryimagessettings",
            name="rescaler_fallback_jpeg",
            field=models.BooleanField(
                default=True,
                help_text="When other formats are enabled; also generate a JPEG fallback for older browsers.",
                verbose_name="Enable JPEG Fallback",
            ),
        ),
    ]