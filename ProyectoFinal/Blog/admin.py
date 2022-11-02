from django.contrib import admin
from Blog.models import Autores, Articulos, Secciones, Avatar

# Register your models here.
admin.site.register(Autores)
admin.site.register(Articulos)
admin.site.register(Secciones)
admin.site.register(Avatar)
