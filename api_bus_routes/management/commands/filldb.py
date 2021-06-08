from django.core.management.base import BaseCommand
from api_bus_routes.models import RouteModel


def normalized_data(date: str):
    new_date = date.split('.')
    return new_date[2] + '-' + new_date[1] + '-' + new_date[0]


def parse_csv(csv_name: str):
    RouteModel.objects.all().delete()
    with open(csv_name, 'r') as f:
        for row in f:
            try:
                data = row.split(';')
                route = data[2].split('-')
                for i in range(len(route)):
                    route[i] = route[i].strip()

                model = RouteModel.objects.create(id=int(data[0]),
                                                  rf_subject=data[1].strip(),
                                                  transportation_route=route,
                                                  route_number=data[3].strip(),
                                                  carrier=data[4].strip(),
                                                  date_of_entry=normalized_data(data[5]),
                                                  registry_number=data[6].strip(),
                                                  destination=data[7].strip(),
                                                  destination_code=int(data[8]))
                model.save()
            except Exception as e:
                print(e)


class Command(BaseCommand):
    def handle(self, *args, **options):
        parse_csv('data/route_data.csv')
