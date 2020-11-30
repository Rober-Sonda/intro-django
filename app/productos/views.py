from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productos.models import Productos
from carrito.carrito import Carrito

# Create your views here.
@login_required(login_url='autenticacion/acceder')
def list_products(request):
    carrito = Carrito(request)
    products = Productos.objects.all()
    return render(request, "productos/listado.html", {
        "products": products
    })