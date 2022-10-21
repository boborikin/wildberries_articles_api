from django.db import models


class Product(models.Model):
    """Модель базы данных, для хранения необходимой информации о товаре."""
    article = models.IntegerField(unique=True)
    brand = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
