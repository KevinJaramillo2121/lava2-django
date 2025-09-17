from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
        ('client', 'Cliente'),
    )

    # Campos adicionales para el registro
    documento_identidad = models.CharField(max_length=20, unique=True, null=True, blank=True)
    nombre_completo = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    # Rol del usuario, por defecto será 'cliente'
    rol = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username


class Vehiculo(models.Model):
    propietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
