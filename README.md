Sistema de Gestión para Lavadero de Autos - Lava2
Lava2 es una aplicación web desarrollada con Django, diseñada para ser un sistema integral de gestión para un lavadero de autos. Permite manejar clientes, empleados y administradores, cada uno con su propio panel y funcionalidades específicas. El proyecto está construido siguiendo las mejores prácticas de Django, con una arquitectura modular y escalable.

Características Principales
Sistema de Autenticación Personalizado: Manejo de registro, inicio y cierre de sesión.

Gestión de Roles: Tres roles de usuario predefinidos: admin, employee y client.

Redirección Dinámica por Rol: Cada usuario es dirigido a un panel de control (dashboard) específico según su rol después de iniciar sesión.

Registro de Clientes y Vehículos: Los nuevos clientes se registran junto con su primer vehículo.

Panel de Administración Personalizado: Panel de Django (/admin/) configurado para gestionar usuarios y sus campos personalizados.

Módulo de Reservas para Clientes:

Los clientes pueden agendar un servicio de lavado desde su panel.

Selección de vehículo, tipo de lavado (con precios), y productos adicionales opcionales.

Posibilidad de elegir un empleado específico (mostrando su calificación y experiencia) o permitir que el sistema asigne uno automáticamente.

Tecnologías Utilizadas
Backend: Django

Base de Datos: PostgreSQL

Frontend: HTML5, CSS3 (plantillas de Django)

Entorno: Python, venv

Instalación y Puesta en Marcha
Sigue estos pasos para configurar el entorno de desarrollo en tu máquina local.

1. Clonar el Repositorio
bash
git clone <URL-del-repositorio>
cd lava2
2. Configurar el Entorno Virtual
Crear el entorno virtual:

bash
python -m venv venv
Activar el entorno:

En Windows:

bash
.\venv\Scripts\activate
En macOS/Linux:

bash
source venv/bin/activate
3. Instalar Dependencias
bash
pip install -r requirements.txt
4. Configurar la Base de Datos y Variables de Entorno
a. Prepara tu base de datos PostgreSQL:

sql
CREATE DATABASE lava2db;
CREATE USER lava2user WITH PASSWORD 'tu-clave-segura';
GRANT ALL PRIVILEGES ON DATABASE lava2db TO lava2user;
b. Crea el archivo .env:
En la raíz del proyecto, crea un archivo .env y añade tu configuración.

text
# Ejemplo de archivo .env
SECRET_KEY='tu-nueva-clave-secreta-aqui'
DATABASE_URL='postgres://lava2user:tu-clave-segura@localhost:5432/lava2db'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' # Para desarrollo
Nota: Se utiliza dj-database-url para simplificar la configuración de la base de datos.

5. Ejecutar Migraciones y Crear Superusuario
bash
# Aplica las migraciones para crear las tablas en la base de datos
python manage.py migrate

# Crea un superusuario para acceder al panel de administración de Django
python manage.py createsuperuser
6. Lanzar el Servidor
bash
python manage.py runserver
¡Ahora puedes acceder a la aplicación en http://127.0.0.1:8000/!

Estructura del Proyecto
La arquitectura del proyecto está dividida en aplicaciones modulares para una mejor organización y escalabilidad.

text
lava2/
├── core/             # App principal (settings.py, urls.py)
├── accounts/         # App para autenticación y gestión de usuarios
├── reservations/     # App para el sistema de reservas de lavados
├── templates/        # Directorio global de plantillas
│   ├── base.html
│   ├── dashboards/
│   └── reservations/
├── static/           # Archivos estáticos (CSS, JS, imágenes)
├── .env              # Variables de entorno (ignorado por Git)
├── manage.py
└── requirements.txt


Próximos Pasos
Con la base de la aplicación y el módulo de reservas establecidos, los siguientes pasos se centrarán en enriquecer la experiencia de los usuarios:

Dashboard del Cliente: Mostrar el historial de reservas (pendientes, en proceso, completadas).

Dashboard del Empleado: Permitir a los empleados ver y gestionar los lavados que tienen asignados (cambiar estado, ver detalles).

Notificaciones: Implementar un sistema de notificaciones por correo o en la plataforma al confirmar o finalizar una reserva.

Calificaciones: Permitir que los clientes califiquen el servicio una vez completado, actualizando la calificación del empleado.