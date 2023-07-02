from django import forms
from django.contrib.auth.models import User
from SPL.models import *

class SerieFormulario(forms.Form):

    nombre = forms.CharField()
    genero = forms.CharField()
    director = forms.CharField()
    año = forms.IntegerField()


class PeliFormulario(forms.Form):

    nombre = forms.CharField()
    genero = forms.CharField()
    director = forms.CharField()
    año = forms.IntegerField()


class LibroFormulario(forms.Form):

    nombre = forms.CharField()
    genero = forms.CharField()
    autor = forms.CharField()
    año = forms.IntegerField()
