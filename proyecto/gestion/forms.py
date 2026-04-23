from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "correo", "nacionalidad", "fecha_nacimiento", "biografia"]


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "fecha_publicacion", "genero", "isbn", "autor"]