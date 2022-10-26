from django.db import models

# Create your models here.


class Secciones(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    categoria = models.CharField(max_length=100)    
    def __str__(self):
        return self.categoria


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
    fecha_de_publicacion = models.DateField(null=True)

    def __str__(self):
        return self.titulo

