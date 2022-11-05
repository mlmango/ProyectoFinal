from django.contrib import admin

# Register your models here.

from Mensajes.models import Message

admin.site.register(Message)