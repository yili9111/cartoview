# Generated by Django 2.1.3 on 2019-03-19 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_auto_20190319_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='center',
            field=models.CharField(max_length=150),
        ),
    ]