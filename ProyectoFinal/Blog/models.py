from django.db import models

# Create your models here.


class Autores(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Articulos(models.Model):
    class Meta:
        verbose_name_plural = "Articulos"

    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    articulo_nro = models.IntegerField()
    username_autor = models.CharField(max_length=100)
    fecha_de_publicacion = models.DateField()

    def __str__(self):
        return (f"Articulo {self.titulo}, de {self.username_autor}, con fecha de publicación {self.fecha_de_publicacion}")


class Secciones(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre