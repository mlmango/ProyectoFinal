from django.urls import path
from Blog.views import busqueda_bd, mostrar_inicio, procesar_formulario_articulo, procesar_formulario_autor, procesar_formulario_seccion, mapa_del_sitio

urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("busqueda-art/", busqueda_bd),
    path("map/", mapa_del_sitio),
    


]