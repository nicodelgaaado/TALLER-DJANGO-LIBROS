from django.shortcuts import get_object_or_404, redirect, render

from .forms import LibroForm
from .models import Libro


# ===== CRUD AUTORES =====
# Mantener en esta seccion el CRUD existente de Autor.


# ===== CRUD LIBROS (OSKAR) =====
def leer_libros(request):
    """Lee y muestra el listado completo de libros."""
    libros = Libro.objects.all()
    return render(request, "gestion/lista_libros.html", {"libros": libros})


def crear_libro(request):
    """Crea un nuevo libro usando el formulario del modulo."""
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leer_libros")
    else:
        form = LibroForm()

    return render(request, "gestion/libro_form.html", {"form": form})


def actualizar_libro(request, pk):
    """Actualiza un libro existente identificado por su clave primaria."""
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("leer_libros")
    else:
        form = LibroForm(instance=libro)

    return render(
        request,
        "gestion/libro_form.html",
        {"form": form, "libro": libro},
    )


def eliminar_libro(request, pk):
    """Solicita confirmacion y elimina un libro cuando llega un POST."""
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == "POST":
        libro.delete()
        return redirect("leer_libros")

    return render(
        request,
        "gestion/libro_confirm_delete.html",
        {"libro": libro},
    )


# Alias opcionales para mantener compatibilidad si ya existen rutas antiguas.
lista_libros = leer_libros
editar_libro = actualizar_libro
