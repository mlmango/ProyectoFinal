from django.http import HttpResponse
from django.shortcuts import render
from Blog.forms import (
    formulario_Articulos,
    formulario_Autores,
    formulario_Secciones,
    AvatarForm,
    UserEditionForm,
)
from Blog.models import Articulos, Autores, Secciones, User, Avatar
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.


@login_required
def busqueda_bd(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.avatar.url}
    else:
        contexto = {}

    if request.method == "GET":
        return render(request, "blog/form-de-busqueda.html", contexto)

    if request.method == "POST":

        dato_ingresado = request.POST["titulo"]
        resultado_busqueda = Articulos.objects.filter(titulo__icontains=dato_ingresado)
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar is not None:
            contexto = {"resultados": resultado_busqueda, "avatar": avatar.avatar.url}
        else:
            contexto = {"resultados": resultado_busqueda}
        return render(request, "blog/resultado-de-busqueda.html", contexto)


@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.avatar.url}
    else:
        contexto = {}

    return render(request, "blog/inicio.html", contexto)



@login_required
def procesar_formulario_autor(request):
    if request.method == "GET":
        mi_formulario = formulario_Autores()
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar is not None:
            contexto = {"formulario": mi_formulario, "avatar": avatar.avatar.url}
        else:
            contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-autor.html", contexto)

    if request.method == "POST":

        mi_formulario = formulario_Autores(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autores(
                nombre=datos_ingresados_por_usuario["nombre"],
                username=datos_ingresados_por_usuario["username"],
                email=datos_ingresados_por_usuario["email"],
            )
            nuevo_modelo.save()

            mi_formulario = formulario_Autores()
            avatar = Avatar.objects.filter(user=request.user).first()
            if avatar is not None:
                contexto = {"formulario": mi_formulario, "avatar": avatar.avatar.url}
            else:
                contexto = {"formulario": mi_formulario}
            return render(request, "blog/formulario-autor-2.html", contexto)
    
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.avatar.url}
    else:
        contexto = {}

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-autor.html", context=contexto)


@login_required
def procesar_formulario_articulo(request):


    if request.method == "GET":
        mi_formulario = formulario_Articulos()
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar is not None:
            contexto = {"formulario": mi_formulario, "avatar": avatar.avatar.url}
        else:
            contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", contexto)

    if request.method == "POST":

        mi_formulario = formulario_Articulos(request.POST, request.FILES)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulos(
                titulo=datos_ingresados_por_usuario["titulo"],
                subtitulo=datos_ingresados_por_usuario["subtitulo"],
                texto=datos_ingresados_por_usuario["texto"],
                articulo_nro=datos_ingresados_por_usuario["articulo_nro"],
                username_autor=datos_ingresados_por_usuario["username_autor"],
                imagen_de_portada=datos_ingresados_por_usuario["imagen_de_portada"],
                fecha_de_publicacion=datos_ingresados_por_usuario[
                    "fecha_de_publicacion"
                ],
            )
            nuevo_modelo.save()

            mi_formulario = formulario_Articulos()
            avatar = Avatar.objects.filter(user=request.user).first()
            if avatar is not None:
                contexto = {"formulario": mi_formulario, "avatar": avatar.avatar.url}
            else:
                contexto = {"formulario": mi_formulario}
            return render(request, "blog/formulario-articulo-2.html", contexto)


    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-articulo.html", context=contexto)


class ArticulosList(LoginRequiredMixin, ListView):
    model = Articulos
    template_name = "blog/pages.html"


@login_required
def about_us(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.avatar.url}
    else:
        contexto = {}

    return render(request, "blog/about.html", contexto)


class ArticuloDetail(LoginRequiredMixin, DetailView):
    model = Articulos
    template_name = "blog/detalle.html"


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulos
    success_url = "/blog/pages/"
    fields = [
        "titulo",
        "subtitulo",
        "texto",
        "articulo_nro",
        "username_autor",
        "imagen_de_portada",
        "fecha_de_publicacion",
    ]


class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulos
    success_url = "/blog/pages/"


class MyLogin(LoginView):
    template_name = "blog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request, "Blog/inicio.html", {"mensaje": f"{username_capturado}"}
            )

    else:
        form = UserCreationForm()

    return render(request, "Blog/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            if avatar is not None:
                contexto = {"mensajeEdicion": "Usuario editado, por favor ingrese nuevamente", "avatar": avatar.avatar.url}
            else:
                contexto = {"mensajeEdicion": "Usuario editado, por favor ingrese nuevamente",}
            return render(request, "Blog/inicio.html", contexto)

    if avatar is not None:
        contexto = {"user": user, "form": form, "avatar": avatar.avatar.url}
    else:
        contexto = {"user": user, "form": form}
    return render(request, "Blog/editperfil.html", contexto)



@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "Blog/inicio.html")

    contexto = {"form": form}
    return render(request, "Blog/cambiarAvatar.html", contexto)
