from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_num')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'table', 'created_at')
