# django-rest-api

## API для доступа к Реестру регулярных автобусных маршрутов между субъектами Российской Федерации

Сервис, который популяризирует открытые данные в России. 
Одна из задач сервиса — предоставить доступ к открытым данным 
для сторонних разработчиков через HTTP API, чтобы как можно больше 
компаний использовали открытые данные в своих проектах.

1. За основу взята таблца с сайта https://data.gov.ru, которую можно найти по адресу https://data.gov.ru/opendata/7705851331-reestrautorf
2. Написан парсер, который запускается с docker-compose up

Также его можно запустить командой 
```console
$ python manage.py filldb
```
3. Документация к API доступна по ссылке https://app.swaggerhub.com/apis/Dimkashow/BusRoutesApi/1.0.0
4. Docker образ досутпен по ссылке https://hub.docker.com/repository/docker/dimkov27/rest_api_web

Для того, чтобы заустить проект выполните команды
```console
$ docker-compose up -d --build
$ docker-compose up
```

Демонстрация работы API
```console
$ curl http://0.0.0.0:8000/api/routes/findroute/Чебоксары/Яльчики/
[{"id":2,"rf_subject":"Чувашская Республика","transportation_route":["Чебоксары","Яльчики","Ульяновск(н.Город)"],"route_number":"587","carrier":"Чувашавтотранс ГУП ЧР","date_of_entry":"2007-04-04","registry_number":"73-04","destination":"Ульяновская обл","destination_code":73},{"id":2397,"rf_subject":"Чувашская Республика","transportation_route":["Чебоксары","Яльчики","Буинск","Ульяновск"],"route_number":"587","carrier":"\"ООО \"\"Транспортная компания \"\"С-путник\"\"\"","date_of_entry":"2008-10-14","registry_number":"21-49","destination":"Ульяновская обл","destination_code":73}]%
```
 
Для работы с API, которые изменяют/удаляют данные, необходимо в ссылку добавить query param ?api_key=test test - тестовый токен
Демонстрация работы API
```console
$ curl -X DELETE http://0.0.0.0:8000/api/routes/delete/10/
{"detail":"Not found."}%

$ curl -X DELETE http://0.0.0.0:8000/api/routes/delete/10/\?api_key\=test
"Deleted"%
```
