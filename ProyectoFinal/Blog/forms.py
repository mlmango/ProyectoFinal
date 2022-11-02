from mailbox import NoSuchMailboxError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Blog.models import Autores, Articulos, Secciones, Avatar

class formulario_Autores(forms.Form):
    nombre=forms.CharField(max_length=100)
    username=forms.CharField(max_length=50)
    email=forms.EmailField()

class formulario_Articulos(forms.Form):
    FANTASIA = 'fant'
    CODING = 'coder'
    LIFESTYLE = 'vida'
    sections = (
        ('', '----'),
        (FANTASIA, 'Fantasía'),
        (CODING, 'Coding'),
        (LIFESTYLE, 'Estilo de vida'),
    )
    titulo=forms.CharField(max_length=100)
    texto=forms.CharField(max_length=1000)
    articulo_nro=forms.IntegerField()
    username_autor=forms.ModelChoiceField(
        required=True,
        queryset=Autores.objects.all(),
        label="Username del Autor")
    fecha_de_publicacion=forms.DateField()
#    seccion=forms.ModelChoiceField(
#        required=False,
#        queryset=Secciones.objects.all(),
#        label="Sección"
#    )

class formulario_Secciones(forms.Form):
    categoria=forms.CharField(max_length=100)


class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    username = forms.CharField(label="Nombre de usuario")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name", "username"]


class AvatarForm(forms.ModelForm):

    avatar = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["avatar", "user"]