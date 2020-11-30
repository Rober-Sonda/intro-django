from django.urls import path
from .views import *


app_name = "cart"

urlpatterns = [
    path('agregarproducto/<int:producto_id>', add_product, name="add_product"),
    path('removerproducto/<int:producto_id>', remove_product, name="remove_product"),
    path('decrementarproducto/<int:producto_id>', decrement_product, name="decrement_product"),
    path('limpiarcarrito', clear_cart, name="clear_cart"),
]
