# CiberDuo

CiberDuo es una aplicación web educativa desarrollada con Django para
presentar cuestionarios de ciberseguridad organizados por perfiles.

## Funcionalidades

- Registro e inicio de sesión de usuarios.
- Dashboard con los perfiles disponibles.
- Preguntas organizadas por perfil.
- Respuestas de selección múltiple con retroalimentación.
- Historial de respuestas del usuario.
- Panel de administración para gestionar:
  - Perfiles.
  - Preguntas.
  - Opciones de respuesta.
  - Tipos de amenaza.
  - Medios.
- Control de intentos fallidos de inicio de sesión mediante Django Axes.
- Consentimiento de cookies.
- Preferencia de modo claro u oscuro guardada en cookies.

## Tecnologías

- Python 3.10 o superior.
- Django 4.2.30.
- MySQL.
- Bootstrap 5.
- Django Axes.

## Requisitos previos

Antes de ejecutar el proyecto debes tener instalado:

- Python.
- MySQL Server.
- Las herramientas necesarias para compilar `mysqlclient` en tu sistema.

También debes crear una base de datos llamada `ciberduo` en MySQL:

```sql
CREATE DATABASE ciberduo;
```

## Instalación

1. Clona o descarga el proyecto.

2. Entra en la carpeta principal:

```bash
cd Eva2-Viernes
```

3. Crea y activa un entorno virtual:

```bash
python -m venv venv
```

En Windows:

```bash
venv\Scripts\activate
```

En macOS o Linux:

```bash
source venv/bin/activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

5. Configura la conexión a MySQL en `CiberDuo/settings.py` si tus datos
   de usuario, contraseña, host o puerto son diferentes.

6. Ejecuta las migraciones:

```bash
python manage.py migrate
```

7. Crea un usuario administrador:

```bash
python manage.py createsuperuser
```

8. Inicia el servidor:

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

## Uso de la aplicación

1. Accede al formulario de inicio de sesión.
2. Después de iniciar sesión, selecciona un perfil desde el dashboard.
3. Responde las preguntas asociadas al perfil.
4. Consulta tus resultados desde **Mi historial**.

Los usuarios administradores pueden acceder al panel de administración
desde el enlace disponible en el dashboard.

## Estructura principal

```text
Eva2-Viernes/
├── CiberDuo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── contenido/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── static/contenido/estilos.css
│   └── templates/contenido/
├── manage.py
├── requirements.txt
└── README.md
```

## Comandos útiles

Comprobar la configuración de Django:

```bash
python manage.py check
```

Crear nuevas migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

## Nota de seguridad

Antes de utilizar la aplicación en producción, cambia la `SECRET_KEY`,
desactiva `DEBUG`, configura `ALLOWED_HOSTS` y utiliza credenciales seguras
para la base de datos.
