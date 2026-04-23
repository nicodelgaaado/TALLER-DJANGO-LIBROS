from django.urls import path

from . import views


urlpatterns = [
    path("libros/", views.leer_libros, name="leer_libros"),
    path("libros/crear/", views.crear_libro, name="crear_libro"),
    path("libros/editar/<int:pk>/", views.actualizar_libro, name="actualizar_libro"),
    path("libros/eliminar/<int:pk>/", views.eliminar_libro, name="eliminar_libro"),
]
