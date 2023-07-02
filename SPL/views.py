from django.shortcuts import render
from SPL.models import *
from SPL.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
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

        return render(request, "SPL/resultadoSeries.html", {"series":series, "nombre":nombre})

    else:
        respuesta = "No enviaste ningún dato."
    
    return HttpResponse(respuesta)

def busquedaPeli(request):

    return render(request, "SPL/busquedaPeli.html")

def resultadoPeli(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        pelis = Pelicula.objects.filter(nombre__icontains=nombre)

        return render(request, "SPL/resultadoPeli.html", {"pelis":pelis, "nombre":nombre})

    else:
        respuesta = "No enviaste ningún dato."
    
    return HttpResponse(respuesta)

def busquedaLibro(request):

    return render(request, "SPL/busquedaLibro.html")

def resultadoLibro(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        libros = Libro.objects.filter(nombre__icontains=nombre)

        return render(request, "SPL/resultadoLibro.html", {"libros":libros, "nombre":nombre})

    else:
        respuesta = "No enviaste ningún dato."
    
    return HttpResponse(respuesta)

def about(request):

    return render(request, 'SPL/about.html')

def borrar_pelis(request, peli_nombre):
    
    peli_elegida = Pelicula.objects.get(nombre=peli_nombre)
    peli_elegida.delete()

    return render(request, "SPL/inicio.html")

def borrar_series(request, serie_nombre):
    
    serie_elegida = Serie.objects.get(nombre=serie_nombre)
    serie_elegida.delete()

    return render(request, "SPL/inicio.html")

def borrar_libros(request, libro_nombre):
    
    libro_elegido = Libro.objects.get(nombre=libro_nombre)
    libro_elegido.delete()

    return render(request, "SPL/inicio.html")

def editar_peli(request, peli_nombre):

    peli_elegida = Pelicula.objects.get(nombre=peli_nombre)

    if request.method == "POST":

        formulario = PeliFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            info = formulario.cleaned_data

            peli_elegida.nombre = info["nombre"]
            peli_elegida.genero = info["genero"]
            peli_elegida.director = info["director"]
            peli_elegida.año = info["año"]

            peli_elegida.save()

            return render(request, 'SPL/inicio.html')
    else:

        miFormulario = PeliFormulario(initial={"nombre": peli_elegida.nombre,
                                               "genero": peli_elegida.genero,
                                               "director": peli_elegida.director,
                                               "año": peli_elegida.año})

    return render(request, "SPL/editarpeli.html", {"form2": miFormulario})
        
def editar_serie(request, serie_nombre):

    serie_elegida = Serie.objects.get(nombre=serie_nombre)

    if request.method == "POST":

        formulario = SerieFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            info = formulario.cleaned_data

            serie_elegida.nombre = info["nombre"]
            serie_elegida.genero = info["genero"]
            serie_elegida.director = info["director"]
            serie_elegida.año = info["año"]

            serie_elegida.save()

            return render(request, 'SPL/inicio.html')
        
    else:

        miFormulario = SerieFormulario(initial={"nombre": serie_elegida.nombre,
                                               "genero": serie_elegida.genero,
                                               "director": serie_elegida.director,
                                               "año": serie_elegida.año})

    return render(request, "SPL/editarserie.html", {"form1": miFormulario})
        
def editar_libro(request, libro_nombre):

    libro_elegido = Libro.objects.get(nombre=libro_nombre)

    if request.method == "POST":

        formulario = LibroFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            info = formulario.cleaned_data

            libro_elegido.nombre = info["nombre"]
            libro_elegido.genero = info["genero"]
            libro_elegido.autor = info["autor"]
            libro_elegido.año = info["año"]

            libro_elegido.save()

            return render(request, 'SPL/inicio.html')
    
    else:

        miFormulario = LibroFormulario(initial={"nombre": libro_elegido.nombre,
                                               "genero": libro_elegido.genero,
                                               "autor": libro_elegido.autor,
                                               "año": libro_elegido.año})

    return render(request, "SPL/editarlibro.html", {"form3": miFormulario})