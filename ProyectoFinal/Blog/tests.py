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
            fecha_de_publicacion=ahora,
        )
        todos_los_articulos = Articulos.objects.all()
        assert len(todos_los_articulos) == 1
        assert articulo == todos_los_articulos[0]

    def test_crear_autor(self):
        autor = Autores.objects.create(
            nombre="autor test1", username="autortest1", email="autor@test1.com"
        )
        todos_los_autores = Autores.objects.all()
        assert len(todos_los_autores) == 1
        assert autor == todos_los_autores[0]

    def test_crear_articulo_sin_fecha(self):
        Articulos.objects.create(
            titulo="test1",
            texto="test nro 1 hola!",
            articulo_nro="1",
            username_autor="mlmango",
        )
        todos_los_articulos = Articulos.objects.all()
        assert todos_los_articulos[0].fecha_de_publicacion is None

    def test_varios_articulo(self):
        ahora = datetime.now()
        Articulos.objects.create(
            titulo="test1",
            texto="test nro 1 hola!",
            articulo_nro="1",
            username_autor="mlmango",
            fecha_de_publicacion=ahora,
        )
        Articulos.objects.create(
            titulo="test2",
            texto="test nro 2 hola!",
            articulo_nro="2",
            username_autor="olivetta",
            fecha_de_publicacion="2022-10-31",
        )
        Articulos.objects.create(
            titulo="test3",
            texto="test nro 3 hola!",
            articulo_nro="3",
            username_autor="gmichael",
            fecha_de_publicacion=ahora,
        )
        todos_los_articulos = Articulos.objects.all()
        assert len(todos_los_articulos) == 3
