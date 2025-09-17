from django.urls import path
from .views import (
    SignUpView, 
    AdminDashboardView, 
    EmployeeDashboardView, 
    ClientDashboardView,
    redirect_after_login  # Importamos la función de redirección
)

urlpatterns = [
    # Ruta para el registro de nuevos usuarios
    path('signup/', SignUpView.as_view(), name='signup'),
    
    # --- URLs para los paneles de cada rol ---
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('dashboard/employee/', EmployeeDashboardView.as_view(), name='employee_dashboard'),
    path('dashboard/client/', ClientDashboardView.as_view(), name='client_dashboard'),

    # --- URL para la vista "despachador" que redirige según el rol ---
    path('redirect/', redirect_after_login, name='login_redirect'), # Esta era la línea con el error
]
# Nota: La URL 'redirect/' es una vista que redirige al usuario al dashboard correspondiente según su rol.