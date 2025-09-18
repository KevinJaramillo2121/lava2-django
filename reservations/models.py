from django.db import models
from django.conf import settings
from django.utils import timezone # Importar timezone

# --- NUEVO MODELO ---
# Modelo para las Sedes o sucursales del lavadero
class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    # Podríamos añadir más campos como teléfono, horario de apertura, etc.

    def __str__(self):
        return self.nombre

# --- MODELO MODIFICADO ---
# Modelo para guardar datos adicionales del empleado
class EmpleadoProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='empleado_profile',
        limit_choices_to={'rol': 'employee'}
    )
    # --- NUEVO CAMPO ---
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True, related_name='empleados')
    experiencia = models.TextField(blank=True, help_text="Describe la experiencia del empleado.")
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# ... (El modelo TipoLavado y Producto no cambian) ...
class TipoLavado(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - ${self.precio:,.0f}"

class Producto(models.Model):
    CATEGORIAS = [
        ('shampoo', 'Shampoo'),
        ('cera', 'Cera'),
        ('silicona', 'Silicona'),
        ('partes_negras', 'Protección de Partes Negras'),
        ('cuidado_pintura', 'Cuidado de Pintura'),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    
    def __str__(self):
        return f"{self.get_categoria_display()}: {self.nombre}"

# --- MODELO MODIFICADO ---
# Modelo principal que une todo: la Reserva
class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reservas',
        limit_choices_to={'rol': 'client'}
    )
    # --- NUEVO CAMPO ---
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT,)
    vehiculo = models.ForeignKey('accounts.Vehiculo', on_delete=models.CASCADE)
    empleado_asignado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='lavados_asignados',
        limit_choices_to={'rol': 'employee'}
    )
    tipo_lavado = models.ForeignKey(TipoLavado, on_delete=models.PROTECT)
    productos = models.ManyToManyField(Producto, blank=True)
    # --- CAMPO MODIFICADO ---
    # Ya no se autocompleta, el cliente elegirá la fecha y hora de su cita.
    fecha_hora_cita = models.DateTimeField()
    fecha_creacion = models.DateTimeField(default=timezone.now) # Mantenemos un registro de cuándo se creó
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Reserva de {self.cliente.username} en {self.sede.nombre} para el {self.fecha_hora_cita.strftime('%Y-%m-%d %H:%M')}"

