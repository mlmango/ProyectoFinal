from django.shortcuts import render
from Blog.forms import formulario_Articulos , formulario_Autores , formulario_Secciones
from Blog.models import Articulos, Autores, Secciones


# Create your views here.

def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario_autor(request):
    if request.method == 'GET':
        mi_formulario = formulario_Autores()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-autor.html", context=contexto)

    if request.method == 'POST':

        mi_formulario = formulario_Autores(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autores(
                nombre=datos_ingresados_por_usuario["nombre"],
                username=datos_ingresados_por_usuario["username"],
                email=datos_ingresados_por_usuario["email"] 
            )
            nuevo_modelo.save()
            
            mi_formulario = formulario_Autores()
            contexto = {"formulario": mi_formulario}
            return render(request, "blog/formulario-autor.html", context=contexto)

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-autor.html", context=contexto)


def procesar_formulario_articulo(request):
    if request.method == 'GET':
        mi_formulario = formulario_Articulos()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)

    if request.method == 'POST':

        mi_formulario = formulario_Articulos(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulos(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                articulo_nro=datos_ingresados_por_usuario["articulo_nro"],
                username_autor=datos_ingresados_por_usuario["username_autor"],
                fecha_de_publicacion=datos_ingresados_por_usuario["fecha_de_publicacion"]  
            )
            nuevo_modelo.save()
            
            mi_formulario = formulario_Articulos()
            contexto = {"formulario": mi_formulario}
            return render(request, "blog/formulario-articulo.html", context=contexto)

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-articulo.html", context=contexto)
    

def procesar_formulario_seccion(request):
    if request.method == 'GET':
        mi_formulario = formulario_Secciones()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-seccion.html", context=contexto)

    if request.method == 'POST':

        mi_formulario = formulario_Secciones(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Secciones(
                nombre=datos_ingresados_por_usuario["nombre"]  
            )
            nuevo_modelo.save()
            
            mi_formulario = formulario_Secciones()
            contexto = {"formulario": mi_formulario}
            return render(request, "blog/formulario-seccion.html", context=contexto)

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)