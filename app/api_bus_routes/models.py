from django.db import models
from django.contrib.postgres.fields import ArrayField


class RouteModel(models.Model):
    id = models.IntegerField(primary_key=True)
    rf_subject = models.TextField(blank=True, null=True)
    transportation_route = ArrayField(
        models.TextField(blank=True, null=True),
        blank=True, null=True
    )
    route_number = models.TextField(blank=True, null=True)
    carrier = models.TextField(blank=True, null=True)
    date_of_entry = models.DateField(blank=True, null=True)
    registry_number = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    destination_code = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'routes'

    def __str__(self):
        return self.route_number
