# TALLER-DJANGO-LIBROS

Aplicación web desarrollada con Django para la gestión de autores y libros, como parte del taller de Framework Web.

## Características

- Portada principal con métricas del catálogo.
- CRUD completo de autores.
- CRUD completo de libros.
- Relación entre libros y autores.
- Panel administrativo de Django habilitado.
- Configuración para despliegue en Render mediante `render.yaml`.

## Estructura del proyecto

```text
TALLER-DJANGO-LIBROS/
├── proyecto/
│   ├── gestion/            # App principal (modelos, vistas, formularios, tests)
│   ├── proyecto/           # Configuración global de Django
│   ├── manage.py
│   ├── requirements.txt
│   └── build.sh            # Script de build para Render
├── render.yaml             # Blueprint de Render
└── README.md
```

## Requisitos

- Python 3.12+ (en Render se define por variable de entorno).
- `pip`
- Git

## Instalación y ejecución local

1. Clonar el repositorio:

```bash
git clone https://github.com/nicodelgaaado/TALLER-DJANGO-LIBROS.git
cd TALLER-DJANGO-LIBROS/proyecto
```

2. Crear y activar entorno virtual:

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:

```bash
python manage.py migrate
```

5. Levantar servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abrir en navegador:

- App: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Credenciales de administrador

Las credenciales solicitadas para el panel de administración son:

- **username:** `admin`
- **password:** `admin`

> Nota: estas credenciales son solo para entorno académico/desarrollo. En producción deben cambiarse por seguridad.

## Variables de entorno relevantes

La configuración del proyecto utiliza estas variables:

- `DEBUG`
- `SECRET_KEY`
- `DATABASE_URL`
- `ALLOWED_HOSTS` (lista separada por comas)
- `CSRF_TRUSTED_ORIGINS` (lista separada por comas)
- `RENDER_EXTERNAL_HOSTNAME`
- `RENDER_EXTERNAL_URL`

## Pruebas

Para ejecutar el conjunto de pruebas:

```bash
python manage.py test
```

## Despliegue en Render

El proyecto ya incluye `render.yaml` con:

- Servicio web Python (`taller-django-libros-web`)
- Base de datos Postgres (`taller-django-libros-db`)
- Comando de build: `bash build.sh`
- Comando de inicio: `gunicorn proyecto.wsgi:application`

Pasos generales:

1. Asegurar que los cambios estén en la rama remota.
2. Ir al Blueprint en Render y ejecutar **Manual sync**.
3. Verificar que el deploy termine en estado `live`.

## Tecnologías utilizadas

- Django
- Gunicorn
- PostgreSQL (Render)
- WhiteNoise
- dj-database-url

