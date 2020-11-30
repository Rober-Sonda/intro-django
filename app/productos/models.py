from django.db import models

# Model Categoria
class CategoriasProductos(models.Model):
    nombre = models.CharField(max_length=300)
    categoriadestacada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categories_products'
        verbose_name = 'CategoriaProducto'
        verbose_name_plural = 'CategoriasProductos'
        ordering = ['id']

class MarcasProductos(models.Model):
    nombre = models.CharField(max_length=300)
    marcadestacada = models.BooleanField(default=False)
    categoriamarca = models.ForeignKey(CategoriasProductos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'brand_products'
        verbose_name = 'MarcaProducto'
        verbose_name_plural = 'MarcasProductos'
        ordering = ['id']

# Model Products
class Productos(models.Model):
    nombre = models.CharField(max_length=300)
    slug = models.SlugField()
    categoriasproductos = models.ForeignKey(CategoriasProductos, on_delete=models.CASCADE)
    marcasproductos = models.ForeignKey(MarcasProductos, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True)
    extracto = models.TextField(max_length=200, verbose_name='Extracto')
    detalle = models.TextField(max_length=1000, verbose_name='Información del producto')
    precio = models.FloatField()
    precio_costo = models.FloatField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
