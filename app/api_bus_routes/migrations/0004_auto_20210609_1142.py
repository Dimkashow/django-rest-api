# Generated by Django 3.2.4 on 2021-06-09 11:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus_routes', '0003_alter_routemodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routemodel',
            name='carrier',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='date_of_entry',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='destination',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='destination_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='registry_number',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='rf_subject',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='route_number',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='transportation_route',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, size=None),
        ),
    ]