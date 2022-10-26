from django.urls import path
from Blog.views import busqueda_bd, mostrar_inicio, procesar_formulario_articulo, procesar_formulario_autor, procesar_formulario_seccion, mapa_del_sitio
from Blog.views import ArticulosList

urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-autor-2/", procesar_formulario_autor),
    path("formulario-articulo-2/", procesar_formulario_articulo),
    path("formulario-seccion-2/", procesar_formulario_seccion),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("busqueda-art/", busqueda_bd),
    path("map/", mapa_del_sitio),
    path("pages/", ArticulosList.as_view(), name="ArticulosList"),
    


]