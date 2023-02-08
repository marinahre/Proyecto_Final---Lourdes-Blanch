from django import forms

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