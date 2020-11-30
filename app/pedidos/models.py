from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from productos.models import Productos


User = get_user_model()

# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("producto__precio") * F("cantidad"), output_field=FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

class LineaPedido(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"

    class Meta:
        db_table = 'orderlines'
        verbose_name = 'Línea de pedido'
        verbose_name_plural = 'Líneas de pedidos'
        ordering = ['id']

