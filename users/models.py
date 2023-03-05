from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MODERATOR = 'moderator', 'Модератор'
        MEMBER = 'member', 'Пользователь'

    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=30)
    # username = models.CharField(max_length=20)
    # password = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=Roles.choices, default="member")
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField("users.Location", null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
