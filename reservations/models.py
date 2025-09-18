from django.db import models

from django.conf import settings

# Modelo para guardar datos adicionales del empleado
class EmpleadoProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='empleado_profile',
        limit_choices_to={'rol': 'employee'} # Limita a que solo usuarios con rol 'employee' puedan tener perfil
    )
    experiencia = models.TextField(blank=True, help_text="Describe la experiencia del empleado.")
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Modelo para los tipos de lavado
class TipoLavado(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - ${self.precio:,.0f}"

# Modelo para los productos adicionales
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
    # Si los productos tuvieran un costo extra, se añadiría un campo de precio aquí.

    def __str__(self):
        return f"{self.get_categoria_display()}: {self.nombre}"

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
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Reserva de {self.cliente.username} para el {self.fecha_reserva.strftime('%Y-%m-%d %H:%M')}"