from django.db import models

from users.models import User


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    @property
    def author(self):
        return self.author_id.first_name

    @property
    def category(self):
        return self.category_id.name


class Selection(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Ads)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
