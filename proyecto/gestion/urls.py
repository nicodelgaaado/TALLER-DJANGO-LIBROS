from django.urls import path

from . import views


autor_list_view = views.AutorListView.as_view()
autor_create_view = views.AutorCreateView.as_view()
autor_update_view = views.AutorUpdateView.as_view()
autor_delete_view = views.AutorDeleteView.as_view()


urlpatterns = [
    path("libros/", views.leer_libros, name="leer_libros"),
    path("libros/", views.leer_libros, name="lista_libros"),
    path("libros/crear/", views.crear_libro, name="crear_libro"),
    path("libros/editar/<int:pk>/", views.actualizar_libro, name="actualizar_libro"),
    path("libros/editar/<int:pk>/", views.actualizar_libro, name="editar_libro"),
    path("libros/eliminar/<int:pk>/", views.eliminar_libro, name="eliminar_libro"),
    path("autores/", autor_list_view, name="autor_list"),
    path("autores/", autor_list_view, name="lista_autores"),
    path("autores/crear/", autor_create_view, name="autor_create"),
    path("autores/crear/", autor_create_view, name="crear_autor"),
    path("autores/editar/<int:pk>/", autor_update_view, name="autor_update"),
    path("autores/editar/<int:pk>/", autor_update_view, name="editar_autor"),
    path("autores/eliminar/<int:pk>/", autor_delete_view, name="autor_delete"),
    path("autores/eliminar/<int:pk>/", autor_delete_view, name="eliminar_autor"),
]
