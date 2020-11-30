from django.urls import path
from productos.views import list_products

urlpatterns = [
    path('', list_products, name="list_products"),
]
