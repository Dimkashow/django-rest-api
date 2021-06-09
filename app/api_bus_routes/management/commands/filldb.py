from django.core.management.base import BaseCommand
from api_bus_routes.models import RouteModel, AdminCodeModel


def normalized_data(date: str) -> str:
    new_date = date.split('.')
    try:
        return new_date[2] + '-' + new_date[1] + '-' + new_date[0]
    except IndexError as e:
        return ""


def parse_route(route: str) -> list:
    route = route.replace(' ', '')
    route = route.replace('Ростов-на-Дону', 'Ростов_на_Дону')
    route = route.replace('Улан-Удэ', 'Улан_Удэ')
    route = route.replace('Усть-', 'Усть_')
    route = route.replace('Йошкар-Ола', 'Йошкар_Ола')

    route = route.split('-')
    for i in range(len(route)):
        route[i] = route[i].strip()

    return route


def parse_csv(csv_name: str):
    RouteModel.objects.all().delete()
    with open(csv_name, 'r') as f:
        for row in f:
            try:
                data = row.split(';')
                route = parse_route(data[2])
                model = RouteModel.objects.create(id=int(data[0].strip()),
                                                  rf_subject=data[1].strip(),
                                                  transportation_route=route,
                                                  route_number=data[3].strip(),
                                                  carrier=data[4].strip(),
                                                  registry_number=data[6].strip(),
                                                  destination=data[7].strip(),
                                                  destination_code=int(data[8].strip()))

                need_date = normalized_data(data[5])
                if need_date != "":
                    model.date_of_entry = need_date
                model.save()
            except ValueError as e:
                print(e)
        admin_code = AdminCodeModel.objects.create(code="test")
        admin_code.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        parse_csv('data/route_data.csv')

