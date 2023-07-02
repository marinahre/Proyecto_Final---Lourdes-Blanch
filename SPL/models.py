from django.db import models

# Create your models here.

class Serie(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    sinopsis = models.TextField(default=0)

class Pelicula(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    sinopsis = models.TextField(default=0)

class Libro(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    autor = models.CharField(max_length =50)
    año = models.IntegerField()
    sinopsis = models.TextField(default=0)

class sinopsis(models.Model):
    sinopsis = models.TextField()