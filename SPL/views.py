from django.shortcuts import render
from SPL.models import *
from SPL.forms import *
from django.http import HttpResponse
# Create your views here.

def inicio(request):

    return render(request, 'SPL/inicio.html')

def verSeries(request):

    todas_series = Serie.objects.all()

    return render(request, 'SPL/verSeries.html', {'todas_series':todas_series})

def verPelis(request):

    todas_pelis = Pelicula.objects.all()

    return render(request, 'SPL/verPelis.html', {'todas_pelis':todas_pelis})

def verLibros(request):

    todos_libros = Libro.objects.all()

    return render(request, 'SPL/verLibros.html', {'todos_libros':todos_libros})

def agregarSerie(request):

    if request.method == "POST":

        formulario = SerieFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            info = formulario.cleaned_data

            serie = Serie(nombre=info["nombre"], genero=info["genero"], director=info["director"], año=info["año"])

            serie.save()

            return render(request, 'SPL/inicio.html')
    else:
        formulario = SerieFormulario()

    return render(request, "SPL/agregarSerie.html", {"form1":formulario})

def agregarPeli(request):

    if request.method == "POST":

        formulario = PeliFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            info = formulario.cleaned_data

            pelicula = Pelicula(nombre=info["nombre"], genero=info["genero"], director=info["director"], año=info["año"])

            pelicula.save()

            return render(request, 'SPL/inicio.html')
    else:
        formulario = PeliFormulario()


    return render(request, "SPL/agregarPeli.html", {"form2":formulario})

def agregarLibro(request):

    if request.method == "POST":

        formulario = LibroFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            info = formulario.cleaned_data

            libro = Libro(nombre=info["nombre"], genero=info["genero"], autor=info["autor"], año=info["año"])

            libro.save()

            return render(request, 'SPL/inicio.html')
    else:
        formulario = LibroFormulario()


    return render(request, "SPL/agregarLibro.html", {"form3":formulario})

def busquedaSeries(request):

    return render(request, "SPL/busquedaSeries.html")

def resultadoSeries(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        series = Serie.objects.filter(nombre__icontains=nombre)

        return render(request, "SPL/resultadoSeries", {"series":series, "nombre":nombre})

    else:
        respuesta = "No enviaste ningún dato."
    
    return HttpResponse(respuesta)