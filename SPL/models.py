from django.db import models

# Create your models here.

class Serie(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    director = models.CharField(max_length=50)
    año = models.IntegerField()

class Pelicula(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    director = models.CharField(max_length=50)
    año = models.IntegerField()

class Libro(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    autor = models.CharField(max_length =50)
    año = models.IntegerField()