from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


# ===== CRUD AUTORES =====
# Mantener en esta seccion el CRUD existente de Autor.


# ===== CRUD LIBROS (OSKAR) =====
def leer_libros(request):
    """Lee y muestra el listado completo de libros."""
    libros = Libro.objects.select_related("autor").all()
    return render(
        request,
        "gestion/lista_libros.html",
        {
            "libros": libros,
            "total_libros": libros.count(),
            "total_autores": Autor.objects.count(),
        },
    )


def crear_libro(request):
    """Crea un nuevo libro usando el formulario del modulo."""
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_libros")
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
            return redirect("lista_libros")
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
        return redirect("lista_libros")

    return render(
        request,
        "gestion/libro_confirm_delete.html",
        {"libro": libro},
    )


# Alias opcionales para mantener compatibilidad si ya existen rutas antiguas.
lista_libros = leer_libros
editar_libro = actualizar_libro


# ===== VISTAS GENÉRICAS PARA AUTORES =====

class AutorListView(ListView):
    """Lista todos los autores registrados en el sistema."""
    model = Autor
    template_name = "gestion/lista_autores.html"
    context_object_name = "autores"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_autores"] = Autor.objects.count()
        context["total_libros"] = Libro.objects.count()
        return context


class AutorCreateView(CreateView):
    """Permite crear un nuevo autor en el sistema."""
    model = Autor
    form_class = AutorForm
    template_name = "gestion/autor_form.html"
    success_url = reverse_lazy("lista_autores")


class AutorUpdateView(UpdateView):
    """Permite editar los datos de un autor existente."""
    model = Autor
    form_class = AutorForm
    template_name = "gestion/autor_form.html"
    success_url = reverse_lazy("lista_autores")


class AutorDeleteView(DeleteView):
    """Permite eliminar un autor del sistema con confirmación."""
    model = Autor
    context_object_name = "autor"
    template_name = "gestion/autor_confirm_delete.html"
    success_url = reverse_lazy("lista_autores")
