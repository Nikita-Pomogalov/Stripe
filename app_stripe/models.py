from symtable import Class

from django.db import models

class Item(models.Model):
    CURRENT_CURRENCIES = [
        ('usd', 'USD'),
        ('eur', 'EUR'),
        ('rub', 'RU'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENT_CURRENCIES, default='usd')

    def __str__(self):
        return self.name

class Discount(models.Model):
    name = models.CharField(max_length=50)
    percent_off = models.FloatField()
    stripe_coupon_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} ({self.percent_off}%)"

class Tax(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.FloatField()
    stripe_tax_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id}"


# Create your models here.
