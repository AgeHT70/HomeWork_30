from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
