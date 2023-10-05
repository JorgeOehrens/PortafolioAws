from django.db import models
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator

# Create your models here.


class Proyectos(models.Model):
    fecha = models.DateTimeField(default=now, blank=True)
    titulo = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='Proyectos/portadas')

    video = models.FileField(upload_to='Proyectos/videos',null=True)
    def __str__(self):
        return self.titulo
class Profesional(models.Model):
    fecha_creacion = models.DateTimeField(default=now, blank=True)

    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    link_linkedin = models.CharField(max_length=100)
    link_github = models.CharField(max_length=100)

    sobre_mi = models.TextField(default="N/a")
    cv = models.FileField(upload_to='Cv',null=True)

    imagen_profesional = models.ImageField(upload_to='Perfil')

    logo = models.ImageField(upload_to='Logo')

    def __str__(self) -> str:
        return (self.nombre)

class Experiencia (models.Model):
    fecha = models.DateTimeField(default=now, blank=True)
    fecha_duracion = models.CharField(max_length=100)

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    aptitudes = models.CharField(max_length=100)

    descripción = models.TextField(default="N/a")
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
