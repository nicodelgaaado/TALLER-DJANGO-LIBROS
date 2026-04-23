from django.test import TestCase
from django.urls import reverse

from .models import Autor, Libro


class GestionTemplatesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.autor = Autor.objects.create(
            nombre="Gabriel Garcia Marquez",
            correo="gabo@example.com",
            nacionalidad="Colombia",
            fecha_nacimiento="1927-03-06",
            biografia="Autor colombiano destacado por su narrativa latinoamericana.",
        )
        cls.libro = Libro.objects.create(
            titulo="Cien años de soledad",
            fecha_publicacion="1967-05-30",
            genero="Realismo magico",
            isbn="ISBN-0001",
            autor=cls.autor,
        )

    def test_reversa_nombres_canonicos_y_legacy(self):
        self.assertEqual(reverse("lista_autores"), reverse("autor_list"))
        self.assertEqual(reverse("crear_autor"), reverse("autor_create"))
        self.assertEqual(reverse("editar_autor", args=[self.autor.pk]), reverse("autor_update", args=[self.autor.pk]))
        self.assertEqual(reverse("eliminar_autor", args=[self.autor.pk]), reverse("autor_delete", args=[self.autor.pk]))
        self.assertEqual(reverse("lista_libros"), reverse("leer_libros"))
        self.assertEqual(reverse("editar_libro", args=[self.libro.pk]), reverse("actualizar_libro", args=[self.libro.pk]))

    def test_listados_usan_templates_esperados(self):
        respuesta_autores = self.client.get(reverse("lista_autores"))
        respuesta_libros = self.client.get(reverse("lista_libros"))

        self.assertEqual(respuesta_autores.status_code, 200)
        self.assertTemplateUsed(respuesta_autores, "gestion/lista_autores.html")
        self.assertContains(respuesta_autores, "Autores registrados")

        self.assertEqual(respuesta_libros.status_code, 200)
        self.assertTemplateUsed(respuesta_libros, "gestion/lista_libros.html")
        self.assertContains(respuesta_libros, "Libros registrados")

    def test_formularios_usan_templates_esperados(self):
        respuesta_crear_autor = self.client.get(reverse("crear_autor"))
        respuesta_editar_autor = self.client.get(reverse("editar_autor", args=[self.autor.pk]))
        respuesta_crear_libro = self.client.get(reverse("crear_libro"))
        respuesta_editar_libro = self.client.get(reverse("editar_libro", args=[self.libro.pk]))

        self.assertTemplateUsed(respuesta_crear_autor, "gestion/autor_form.html")
        self.assertTemplateUsed(respuesta_editar_autor, "gestion/autor_form.html")
        self.assertTemplateUsed(respuesta_crear_libro, "gestion/libro_form.html")
        self.assertTemplateUsed(respuesta_editar_libro, "gestion/libro_form.html")

    def test_confirmaciones_de_eliminacion_usan_templates_esperados(self):
        respuesta_autor = self.client.get(reverse("eliminar_autor", args=[self.autor.pk]))
        respuesta_libro = self.client.get(reverse("eliminar_libro", args=[self.libro.pk]))

        self.assertTemplateUsed(respuesta_autor, "gestion/autor_confirm_delete.html")
        self.assertTemplateUsed(respuesta_libro, "gestion/libro_confirm_delete.html")

    def test_post_creacion_autor_redirige_al_listado(self):
        respuesta = self.client.post(
            reverse("crear_autor"),
            data={
                "nombre": "Isabel Allende",
                "correo": "isabel@example.com",
                "nacionalidad": "Chile",
                "fecha_nacimiento": "1942-08-02",
                "biografia": "Novelista chilena.",
            },
        )

        self.assertRedirects(respuesta, reverse("lista_autores"))
        self.assertTrue(Autor.objects.filter(correo="isabel@example.com").exists())

    def test_post_creacion_libro_redirige_al_listado(self):
        respuesta = self.client.post(
            reverse("crear_libro"),
            data={
                "titulo": "El otoño del patriarca",
                "fecha_publicacion": "1975-01-01",
                "genero": "Novela",
                "isbn": "ISBN-0002",
                "autor": self.autor.pk,
            },
        )

        self.assertRedirects(respuesta, reverse("lista_libros"))
        self.assertTrue(Libro.objects.filter(isbn="ISBN-0002").exists())

    def test_post_eliminacion_autor(self):
        autor = Autor.objects.create(
            nombre="Mario Vargas Llosa",
            correo="mario@example.com",
            nacionalidad="Peru",
            fecha_nacimiento="1936-03-28",
        )
        respuesta = self.client.post(reverse("eliminar_autor", args=[autor.pk]))

        self.assertRedirects(respuesta, reverse("lista_autores"))
        self.assertFalse(Autor.objects.filter(pk=autor.pk).exists())

    def test_post_eliminacion_libro(self):
        libro = Libro.objects.create(
            titulo="Relato de un naufrago",
            fecha_publicacion="1970-01-01",
            genero="Cronica",
            isbn="ISBN-0003",
            autor=self.autor,
        )
        respuesta = self.client.post(reverse("eliminar_libro", args=[libro.pk]))

        self.assertRedirects(respuesta, reverse("lista_libros"))
        self.assertFalse(Libro.objects.filter(pk=libro.pk).exists())
