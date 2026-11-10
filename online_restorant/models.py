from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Table(models.Model):
    table_num = models.IntegerField(unique=True)


class Dishes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    caption = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)


class Order(models.Model):
    username = models.CharField(max_length=200)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dishes)
    created_at = models.DateTimeField(auto_now_add=True)