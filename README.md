Sistema de Gestión para Lavadero de Autos - "Lava2"
![Django](https://img.shields

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-3

Este repositorio contiene el código fuente de "Lava2", una aplicación web construida con Django para la gestión integral de un lavadero de autos. El proyecto ha evolucionado desde un esqueleto de autenticación básico hasta un sistema con gestión de roles, paneles de control personalizados y una estructura robusta y escalable.

✨ Características Principales
Sistema de Autenticación por Roles:

Tres roles de usuario definidos: Administrador, Empleado y Cliente.

Modelo de usuario (CustomUser) extendido para incluir datos específicos como documento_identidad, nombre_completo y rol.

Paneles de Control (Dashboards) por Rol:

Redirección automática después del login a un panel de control específico según el rol del usuario.

Vistas separadas y protegidas para cada tipo de usuario.

Registro de Clientes y Vehículos:

Formulario de registro público diseñado exclusivamente para que los Clientes creen su cuenta y registren su primer vehículo.

Panel de Administración Completo:

Gestión total de usuarios desde el panel de admin de Django, permitiendo la creación y modificación de cuentas de Administradores y Empleados internamente.

Funcionalidades de Autenticación Estándar:

Inicio de Sesión (Login) y Cierre de Sesión (Logout) seguros (vía POST).

Flujo completo de recuperación y cambio de contraseña.

Base de Datos PostgreSQL: Configurado para usar PostgreSQL, una base de datos potente y lista para producción.

Gestión de Secretos: Implementa un archivo .env para la gestión segura de claves y credenciales fuera del control de versiones.

🚀 Cómo Empezar
Sigue estos pasos para clonar y configurar el proyecto en tu máquina local.

1. Prerrequisitos
Python 3.8+

Git

PostgreSQL

2. Clonar el Repositorio
bash
git clone https://github.com/TuUsuario/lava2-django.git
cd lava2-django
3. Configurar el Entorno Virtual
bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
4. Instalar Dependencias
bash
pip install -r requirements.txt
5. Configurar la Base de Datos y Variables de Entorno
a. Prepara tu base de datos PostgreSQL:

sql
CREATE DATABASE lava2_db;
CREATE USER lava2_user WITH PASSWORD 'tu_clave_segura';
GRANT ALL PRIVILEGES ON DATABASE lava2_db TO lava2_user;
b. Crea el archivo .env:

En la raíz del proyecto, crea un archivo .env y añade tu configuración.

text
# Ejemplo de archivo .env

SECRET_KEY="tu_nueva_clave_secreta_aqui"

# Configuración de la base de datos
DATABASE_URL="postgres://lava2_user:tu_clave_segura@localhost:5432/lava2_db"

# Para desarrollo, los correos se imprimen en consola.
EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"
(Nota: Hemos simplificado la configuración de la base de datos para usar dj-database-url con una sola variable DATABASE_URL, que es una práctica más moderna y compatible con servicios de despliegue).

6. Ejecutar Migraciones y Crear Superusuario
bash
# Aplica las migraciones para crear las tablas en la base de datos
python manage.py migrate

# Crea un superusuario para acceder al panel de administración de Django
python manage.py createsuperuser
7. ¡Lanzar el Servidor!
bash
python manage.py runserver
Ahora puedes acceder a la aplicación en http://127.0.0.1:8000/.

⚙️ Estructura del Proyecto
text
lava2-django/
├── core/                # App principal de configuración
├── accounts/            # App de autenticación y gestión de usuarios
├── templates/
│   ├── base.html
│   ├── dashboards/
│   │   ├── admin_dashboard.html
│   │   ├── client_dashboard.html
│   │   └── employee_dashboard.html
│   └── registration/
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── .env
├── manage.py
├── requirements.txt
└── README.md
下一步 (Próximos Pasos)
Con la base de la aplicación ya establecida, los siguientes pasos se centrarán en construir las funcionalidades principales de negocio, como el agendamiento de servicios, la gestión de lavados por parte de los empleados y la visualización de historiales para los clientes.