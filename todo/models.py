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

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    titulo_academico = models.CharField(max_length=100)
    biografia = models.TextField(max_length=1000)
    correo_electronico = models.CharField(max_length=100)
    dedicacion_personal = models.TextField(max_length=1000)

    def __str__(self):
        return self.nombres