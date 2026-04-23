from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    """Formulario para crear y editar autores."""
    
    class Meta:
        model = Autor
        fields = ["nombre", "correo", "nacionalidad", "fecha_nacimiento", "biografia"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre completo del autor",
                "maxlength": "255"
            }),
            "correo": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "correo@ejemplo.com"
            }),
            "nacionalidad": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Colombia, España, etc."
            }),
            "fecha_nacimiento": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "biografia": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Información adicional del autor...",
                "rows": 4
            }),
        }
        labels = {
            "nombre": "Nombre Completo",
            "correo": "Correo Electrónico",
            "nacionalidad": "Nacionalidad",
            "fecha_nacimiento": "Fecha de Nacimiento",
            "biografia": "Biografía",
        }
        help_texts = {
            "correo": "Debe ser un correo único en el sistema",
            "biografia": "Información opcional sobre el autor",
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre and len(nombre.strip()) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data.get("correo")
        if correo:
            existe = Autor.objects.filter(correo=correo).exclude(pk=self.instance.pk)
            if existe.exists():
                raise forms.ValidationError("Este correo ya está registrado.")
        return correo


class LibroForm(forms.ModelForm):
    """Formulario para crear y editar libros."""
    
    class Meta:
        model = Libro
        fields = ["titulo", "fecha_publicacion", "genero", "isbn", "autor"]
        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título del libro",
                "maxlength": "255"
            }),
            "fecha_publicacion": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "genero": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Ficción, Terror, Fantasía",
            }),
            "isbn": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "ISBN único del libro",
                "maxlength": "20"
            }),
            "autor": forms.Select(attrs={
                "class": "form-control"
            }),
        }
        labels = {
            "titulo": "Título",
            "fecha_publicacion": "Fecha de Publicación",
            "genero": "Género",
            "isbn": "ISBN",
            "autor": "Autor",
        }
        help_texts = {
            "isbn": "Identificador único del libro",
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get("isbn")
        if isbn:
            existe = Libro.objects.filter(isbn=isbn).exclude(pk=self.instance.pk)
            if existe.exists():
                raise forms.ValidationError("Este ISBN ya está registrado.")
        return isbn