from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django import forms

from Blog.models import Secciones

class formulario_Autores(forms.Form):
    nombre=forms.CharField(max_length=100)
    username=forms.CharField(max_length=50)
    email=forms.EmailField()

class formulario_Articulos(forms.Form):
    FANTASIA = 'fant'
    CODING = 'coder'
    LIFESTYLE = 'vida'
    sections = (
        (FANTASIA, 'Fantasía'),
        (CODING, 'Coding'),
        (LIFESTYLE, 'Estilo de vida'),
    )
    titulo=forms.CharField(max_length=100)
    texto=forms.CharField(max_length=1000)
    articulo_nro=forms.IntegerField()
    username_autor=forms.CharField(max_length=100)
    fecha_de_publicacion=forms.DateField()
    seccion=forms.ChoiceField(choices=sections)

class formulario_Secciones(forms.Form):
    categoria=forms.CharField(max_length=30)