from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para el modelo Autor."""
    list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'correo')
    ordering = ('nombre',)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para el modelo Libro."""
    list_display = ('titulo', 'genero', 'fecha_publicacion', 'autor', 'isbn')
    list_filter = ('autor', 'genero', 'fecha_publicacion')
    search_fields = ('titulo', 'isbn')
    ordering = ('titulo',)
