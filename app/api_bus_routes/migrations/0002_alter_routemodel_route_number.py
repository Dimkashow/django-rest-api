# Generated by Django 3.2.4 on 2021-06-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus_routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routemodel',
            name='route_number',
            field=models.TextField(),
        ),
    ]
