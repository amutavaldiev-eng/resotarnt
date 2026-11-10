from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('category/', create_category, name='create_category'),
    path('dishes/', see_dishes, name='see_dishes'),
    path('add_dish/', create_dishes, name='create_dishes'),
    path('update_dish/<int:id>/', update_dishes, name='update_dishes'),
    path('delete_dish/<int:id>/', delete_dishes, name='delete_dishes'),
    path('table/', create_table, name='create_table'),
    path('orders/', see_order, name='see_order'),
    path('add_order/', create_order, name='create_order'),
    path('update_order/<int:id>/', update_order, name='update_order'),
    path('delete_order/<int:id>/', delete_order, name='delete_order'),
]