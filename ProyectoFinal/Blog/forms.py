from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django import forms

class formulario_Autores(forms.Form):
    nombre=forms.CharField(max_length=100)
    username=forms.CharField(max_length=50)
    email=forms.EmailField()

class formulario_Articulos(forms.Form):
    titulo=forms.CharField(max_length=100)
    texto=forms.CharField(max_length=1000)
    articulo_nro=forms.IntegerField()
    username_autor=forms.CharField(max_length=100)
    fecha_de_publicacion=forms.DateField()

class formulario_Secciones(forms.Form):
    nombre=forms.CharField(max_length=30)