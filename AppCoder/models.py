from django.db import models

# Create your models here.
class curso(models.Model):
    curso= models.CharField(max_length=100)
    camada= models.IntegerField()

class estudiantes(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    email= models.CharField(max_length=100)

class profesores(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    profesion=models.CharField(max_length=100)
    email= models.CharField(max_length=100)