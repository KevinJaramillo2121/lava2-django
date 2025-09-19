from django.urls import path
from .views import CrearReservaView, get_empleados_por_sede

app_name = 'reservations' # Esto es importante para el namespacing

urlpatterns = [
    path('crear/', CrearReservaView.as_view(), name='crear_reserva'),
    # En el futuro: path('resumen/<int:pk>/', ResumenReservaView.as_view(), name='resumen_reserva'),

    path('api/get-empleados/', get_empleados_por_sede, name='api_get_empleados'),
]
