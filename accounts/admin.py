# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Vehiculo

class CustomUserAdmin(UserAdmin):
    # Añadimos nuestros campos personalizados a los 'fieldsets'
    # que se muestran en el formulario de edición del usuario.
    fieldsets = UserAdmin.fieldsets + (
        ('Datos Personales', {
            'fields': ('nombre_completo', 'documento_identidad', 'fecha_nacimiento', 'rol')
        }),
    )

    # Hacemos lo mismo para el formulario de creación de un nuevo usuario.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos Personales', {
            'fields': ('nombre_completo', 'documento_identidad', 'fecha_nacimiento', 'rol')
        }),
    )

    # Definimos qué columnas se muestran en la lista de usuarios.
    list_display = ('username', 'email', 'nombre_completo', 'rol', 'is_staff')

# Registramos nuestros modelos en el admin.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Vehiculo)
