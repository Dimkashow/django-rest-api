# Generated by Django 3.2.4 on 2021-06-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bus_routes', '0005_auto_20210609_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
            ],
        ),
    ]
