from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('procesar_pedido', procesar_pedido, name="procesar_pedido"),
    path('me', login_required(listapedido.as_view(), login_url='autenticacion/acceder'), name="listapedido"),
    path('<int:pk>', login_required(detallepedido.as_view(), login_url='autenticacion/acceder'), name="detallepedido"),
]
