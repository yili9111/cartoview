# Generated by Django 2.1.3 on 2019-02-21 14:33

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('license', models.CharField(blank=True, max_length=200, null=True)),
                ('date_installed', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Installed')),
                ('single_instance', models.BooleanField(default=False)),
                ('status', models.CharField(default='Alpha', max_length=100)),
                ('app_img_url', models.TextField(blank=True, max_length=1000, null=True)),
                ('version', models.CharField(max_length=10)),
                ('order', models.IntegerField(default=0, unique=True)),
                ('default_config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'ordering': ['order'],
                'permissions': (('install_app', 'Install App'), ('uninstall_app', 'Uninstall App'), ('change_state', 'Change App State (active, suspend)')),
            },
        ),
        migrations.CreateModel(
            name='AppStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(verbose_name='App Store URL')),
                ('is_default', models.BooleanField(default=False)),
                ('server_type', models.CharField(choices=[('Exchange', 'Exchange'), ('Geoserver', 'Geoserver'), ('QGISServer', 'QGISServer')], default='Geoserver', max_length=256)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='AppType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='app',
            name='category',
            field=models.ManyToManyField(related_name='apps', to='app_manager.AppType'),
        ),
        migrations.AddField(
            model_name='app',
            name='installed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='app',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_manager.AppStore'),
        ),
        migrations.AddField(
            model_name='app',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
