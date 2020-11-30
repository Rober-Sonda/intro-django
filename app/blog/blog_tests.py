'''
test
'''

from config.wsgi import *
from blog.models import Categoria


categorias = Categoria.objects.all()
print("hola")


