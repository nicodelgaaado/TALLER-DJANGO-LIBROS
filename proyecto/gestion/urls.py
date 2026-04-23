from django.urls import path

from . import views


urlpatterns = [
    path("libros/", views.leer_libros, name="leer_libros"),
    path("libros/crear/", views.crear_libro, name="crear_libro"),
    path("libros/editar/<int:pk>/", views.actualizar_libro, name="actualizar_libro"),
    path("libros/eliminar/<int:pk>/", views.eliminar_libro, name="eliminar_libro"),
    
    # Rutas para vistas genéricas de Autor
    path("autores/", views.AutorListView.as_view(), name="autor_list"),
    path("autores/crear/", views.AutorCreateView.as_view(), name="autor_create"),
    path("autores/editar/<int:pk>/", views.AutorUpdateView.as_view(), name="autor_update"),
    path("autores/eliminar/<int:pk>/", views.AutorDeleteView.as_view(), name="autor_delete"),
]
