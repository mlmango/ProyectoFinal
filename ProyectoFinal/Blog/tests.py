from datetime import datetime
from django.test import TestCase
from Blog.models import Articulos, Autores

# Create your tests here.

class ViewTestCase(TestCase):
    def test_crear_articulo(self):
        ahora = datetime.now()
        articulo = Articulos.objects.create(
            titulo="test1",
            texto="test nro 1 hola!",
            articulo_nro="1",
            username_autor="mlmango",
            fecha_de_publicacion=ahora
        )
        todos_los_articulos = Articulos.objects.all()
        assert len(todos_los_articulos) == 1
        assert articulo == todos_los_articulos[0]