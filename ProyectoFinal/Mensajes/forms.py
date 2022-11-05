from django import forms
from django.contrib.auth.models import User

class enviar_mensaje_form(forms.Form):
    mensaje = forms.CharField(max_length=100)
    username = forms.ModelChoiceField(
        required=True, queryset=User.objects.all(), label="Username Destinatario"
    )