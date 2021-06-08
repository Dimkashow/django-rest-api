from django.db import models
from django.contrib.postgres.fields import ArrayField


class RouteModel(models.Model):
    id = models.IntegerField(primary_key=True)
    rf_subject = models.TextField()
    transportation_route = ArrayField(
        models.TextField()
    )
    route_number = models.TextField()
    carrier = models.TextField()
    date_of_entry = models.DateField()
    registry_number = models.TextField()
    destination = models.TextField()
    destination_code = models.IntegerField()

    class Meta:
        verbose_name_plural = 'routes'

    def __str__(self):
        return self.route_number
