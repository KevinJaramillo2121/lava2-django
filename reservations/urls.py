from django.urls import path
from .views import CrearReservaView

app_name = 'reservations' # Esto es importante para el namespacing

urlpatterns = [
    path('crear/', CrearReservaView.as_view(), name='crear_reserva'),
    # En el futuro: path('resumen/<int:pk>/', ResumenReservaView.as_view(), name='resumen_reserva'),
]
