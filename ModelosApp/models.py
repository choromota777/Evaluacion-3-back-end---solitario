from django.db import models

# Create your models here.
class Employee(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)