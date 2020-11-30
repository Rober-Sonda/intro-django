from django.contrib import admin
from .models import CategoriasProductos, MarcasProductos, Productos

# Register your models here.
admin.site.register([CategoriasProductos, MarcasProductos, Productos])