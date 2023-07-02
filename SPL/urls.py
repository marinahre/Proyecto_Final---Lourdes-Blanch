from django.urls import path, include
from SPL.views import *
from django.conf.urls.static import static
from django.conf import settings
from accounts import *


urlpatterns = [
    path('', inicio, name="Inicio"),

    #Autenticación de usuario


    #Vista
    path('series/', verSeries, name="Series"),
    path('peliculas/', verPelis, name="Pelis"),
    path('libros/', verLibros, name="Libros"),
    path('infoseries/', masInfoSeries, name="infoseries"),

    #Agregar
    path('nuevaserie/', agregarSerie, name="agregar_serie"),
    path('nuevapeli/', agregarPeli, name="agregar_peli"),
    path('nuevolibro/', agregarLibro, name="agregar_libro"),

    #Buscar
    path('busquedaSeries/', busquedaSeries, name="busquedaSeries"),
    path('busquedaSeries/resultadoSeries/', resultadoSeries, name="resultadoSeries"),
    path('busquedaPeli/', busquedaPeli, name="busquedaPeli"),
    path('busquedaPeli/resultadoPeli/', resultadoPeli, name="resultadoPeli"),
    path('busquedaLibro/', busquedaLibro, name="busquedaLibro"),
    path('busquedaLibro/resultadoLibro/', resultadoLibro, name="resultadoLibro"),

    #About
    path('about/', about, name="sobremi"),

    #Eliminar
    path('borrarpeli/<peli_nombre>', borrar_pelis, name="eliminarpeli"),
    path('borrarserie/<serie_nombre>', borrar_series, name="eliminarserie"),
    path('borrarlibro/<libro_nombre>', borrar_libros, name="eliminarlibro"),

    #Editar
    path('editarpeli/<peli_nombre>', editar_peli, name="editar peli"),
    path('editarserie/<serie_nombre>', editar_serie, name="editar serie"),
    path('editarlibro/<libro_nombre>', editar_libro, name="editar libro"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)