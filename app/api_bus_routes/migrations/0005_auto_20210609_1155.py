# Generated by Django 3.2.4 on 2021-06-09 11:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus_routes', '0004_auto_20210609_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routemodel',
            name='carrier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='date_of_entry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='destination',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='destination_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='registry_number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='rf_subject',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='route_number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='transportation_route',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
