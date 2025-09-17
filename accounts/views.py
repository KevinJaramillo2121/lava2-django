from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin # Importa el mixin
from django.shortcuts import redirect # <-- redirect



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirige al login tras el registro exitoso
    template_name = 'registration/signup.html'

# Create your views here.
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/admin_dashboard.html'
    login_url = 'login'

class EmployeeDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/employee_dashboard.html'
    login_url = 'login'

class ClientDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/client_dashboard.html'
    login_url = 'login'


def redirect_after_login(request):
    if request.user.is_authenticated:
        if request.user.rol == 'admin':
            return redirect('admin_dashboard')
        elif request.user.rol == 'employee':
            return redirect('employee_dashboard')
        else: # Por defecto, si es cliente o cualquier otro caso
            return redirect('client_dashboard')
    else:
        # Si por alguna razón un usuario no autenticado llega aquí
        return redirect('login')