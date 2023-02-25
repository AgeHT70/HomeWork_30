# HomeWork_28
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres

./manage.py migrate

./manage.py loaddata fixtures/location.json
./manage.py loaddata fixtures/categories.json
./manage.py loaddata fixtures/users.json
./manage.py loaddata fixtures/ads.json

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
