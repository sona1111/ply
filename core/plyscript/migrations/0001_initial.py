# Generated by Django 4.2.4 on 2023-08-15 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0002_initial'),
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='application/ply.script.generic', max_length=100, verbose_name='Script Type')),
                ('name', models.CharField(max_length=1000, verbose_name='Script Human-readable name')),
                ('descr', models.TextField(verbose_name='Script Description')),
                ('function_name', models.CharField(max_length=1000, verbose_name='Script Function/Callable Name (no spaces)')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Script Created/updated')),
                ('body', models.TextField(verbose_name='Script Body')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'core_plyscript_script',
            },
        ),
        migrations.CreateModel(
            name='ScriptRegistry',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=1000, verbose_name='Registry Key')),
                ('contents_text', models.TextField(verbose_name='Value (Text)')),
                ('contents_json', models.TextField(null=True, verbose_name='Value (JSON)')),
                ('contents_bin', models.BinaryField(null=True, verbose_name='Value (BIN)')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', verbose_name='Profile')),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plyscript.script', verbose_name='Registry')),
            ],
            options={
                'db_table': 'core_plyscript_script_registry',
            },
        ),
        migrations.AddConstraint(
            model_name='scriptregistry',
            constraint=models.UniqueConstraint(fields=('community', 'profile', 'script', 'key'), name='unique_keyperpr'),
        ),
        migrations.AddConstraint(
            model_name='script',
            constraint=models.UniqueConstraint(fields=('community', 'function_name'), name='unique_funcname'),
        ),
        migrations.AddConstraint(
            model_name='script',
            constraint=models.UniqueConstraint(fields=('community', 'name'), name='unique_name'),
        ),
    ]