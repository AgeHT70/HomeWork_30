# HomeWork_28
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres

./manage.py migrate

./manage.py loaddata fixtures/location.json
./manage.py loaddata fixtures/categories.json
./manage.py loaddata fixtures/users.json
./manage.py loaddata fixtures/ads.json

./manage.py runserver
