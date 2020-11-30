from django.shortcuts import redirect
from productos.models import Productos
from django.contrib.auth.decorators import login_required
from .carrito import Carrito


@login_required(login_url="/autenticacion/acceder")
def add_product(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.add(producto=producto)
    return redirect("list_products")


@login_required(login_url="/autenticacion/acceder")
def remove_product(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.remove(producto=producto)
    return redirect("list_products")


@login_required(login_url="/autenticacion/acceder")
def decrement_product(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.decrement(producto=producto)
    return redirect("list_products")


@login_required(login_url="/autenticacion/acceder")
def clear_cart(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect("list_products")
