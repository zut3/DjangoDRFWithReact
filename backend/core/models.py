from django.db import models


class Maker(models.Model):
    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, null=False)
    price = models.FloatField(null=False)

    maker = models.ForeignKey(
        to=Maker,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
