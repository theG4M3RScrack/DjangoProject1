from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)

class Descriptions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

# bien, esta es la clase persona, aqui estan los atributos mencionados en la tarea "https://evirtual.utm.edu.ec/mod/assign/view.php?id=487626"

from django.db import models

class Personas(models.Model):
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    titulo_academico = models.CharField(max_length=100, verbose_name="Titulo Academico")
    biografia = models.TextField(max_length=1000, verbose_name="Biografia")
    correo_electronico = models.CharField(max_length=100, verbose_name="Correo Electronico")
    dedicacion_personal = models.TextField(max_length=1000, verbose_name="Dedicación Personal")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['-created']
        db_table = 'personas'

class Proyectos(models.Model):
    #imagen = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    link = models.URLField(verbose_name="Enlace del proyecto")
    img = models.ImageField(upload_to='projects/', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created'] 
        db_table = 'proyectos'
