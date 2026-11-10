from django.shortcuts import render, redirect
from .models import *

def home_page(request):
    dishes = Dishes.objects.all()
    return render(request, 'home.html', {'dishes': dishes})


def create_category(request):
    if request.method == 'POST':
        Category.objects.create(name = request.POST["name"])
        return redirect('create_category')
    return render(request, 'create_category.html')



def create_table(request):
    if request.method == "POST":
        Table.objects.create(table_num=request.POST["table_num"])
        return redirect('create_table')
    return render(request, 'create_table.html')



def create_dishes(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        Dishes.objects.create(
            category_id=request.POST['category'],
            name=request.POST['name'],
            caption=request.POST['caption'],
            price=request.POST['price']
        )
        return redirect('create_dishes')
    return render(request, 'create_dishes.html', {'categories': categories})



def see_dishes(request):
    dishes = Dishes.objects.all()
    return render(request, 'see_dishes.html', {'dishes': dishes})




def update_dishes(request, id):
    dish = Dishes.objects.get(pk=id)
    categories = Category.objects.all()
    if request.method == "POST":
        dish.name = request.POST["name"]
        dish.caption = request.POST["caption"]
        dish.price = request.POST["price"]
        dish.category_id = request.POST["category"]
        dish.save()
        return redirect('see_dishes')
    return render(request, 'update_dishes.html', {'dish': dish,'categories': categories})


def delete_dishes(request, id):
    dish = Dishes.objects.get(pk=id)
    dish.delete()
    return redirect('see_dishes')                                                                                                  



def create_order(request):
    if request.method == "POST":
        order = Order.objects.create(
            username=request.POST["username"],
            table_id=request.POST["table"])
        order.dishes.add(request.POST["dishes"])
        return redirect('see_order')
    return render(request, 'create_order.html', {'tables': Table.objects.all(),'dishes': Dishes.objects.all()})


def see_order(request):
    orders = Order.objects.all()
    return render(request, 'see_orders.html', {'orders': orders})

def update_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.username = request.POST['username']
        order.table_id = request.POST['table']
        order.save()
        order.dishes.set([request.POST['dishes']])
        return redirect('see_order')
    return render(request, 'update_order.html', {'order': order,'tables': Table.objects.all(),'dishes': Dishes.objects.all()})
def delete_order(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('see_order')                                                                                                  
