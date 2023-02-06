# HomeWork_27
Накатите миграции
Загрузите данные в БД 
./manage.py loaddata ads.json 
./manage.py loaddata ads.json
запустите сервер 
./manage.py runserver

Реализовано:
/cat метод GET, POST
/ad метод GET, POST
/cat/:id метод GET.
/ad/:id метод GET.

Примеры POST-запросов:

POST /cat/
{
	"name": "Кухня"
}

POST /ad/
{
	"name": "Гель для душа",
	"author": "Настя",
	"price": 0,
	"description": "Отдам даром, не подошел", 
	"address": "Москва, метро Коломенская",
	"is_published": false
}
