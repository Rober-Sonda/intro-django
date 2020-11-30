from config.wsgi import *
from blog.models import Categoria

categorias = Categoria.objects.filter(nombre__startswith="J")
print(categorias)

