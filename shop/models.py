from django.db import models


class Sort(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Beer(models.Model):
    beer_name = models.CharField(max_length=255)
    sort = models.ForeignKey(
        Sort,
        null=True,
        on_delete=models.SET_NULL,
        related_name='beers'
    )

    def __str__(self):
        return self.beer_name


class Card(models.Model):
    beer = models.CharField(max_length=255)
    value = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Order(models.Model):
    beer = models.CharField(max_length=255)
    value = models.IntegerField()
    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.SET_NULL,
        related_name='customer'
    )
