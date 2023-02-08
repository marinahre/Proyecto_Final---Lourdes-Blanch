from django.urls import path
from SPL.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('series/', verSeries, name="Series"),
    path('peliculas/', verPelis, name="Pelis"),
    path('libros/', verLibros, name="Libros"),
    path('nuevaserie/', agregarSerie, name="agregar_serie"),
    path('nuevapeli/', agregarPeli, name="agregar_peli"),
    path('nuevolibro/', agregarLibro, name="agregar_libro"),
    path('busquedaSeries/', busquedaSeries, name="busquedaSeries"),
    path('resultadoSeries/', resultadoSeries, name="resultadoSeries"),
]
