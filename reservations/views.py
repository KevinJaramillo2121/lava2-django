from django.http import JsonResponse 
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ReservaForm
from .models import Reserva, EmpleadoProfile
from accounts.models import CustomUser

class CrearReservaView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservations/crear_reserva.html'
    success_url = reverse_lazy('client_dashboard') # Redirige al dashboard del cliente tras el éxito

    def get_form_kwargs(self):
        """Pasa el usuario actual al formulario para filtrar sus vehículos."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        """Añade datos extra al contexto para la plantilla."""
        context = super().get_context_data(**kwargs)
        # Pasamos los perfiles de los empleados para mostrar su información
        context['empleados'] = EmpleadoProfile.objects.filter(user__rol='employee', disponible=True)
        return context

    def form_valid(self, form):
        """Asigna el cliente actual a la reserva antes de guardarla."""
        form.instance.cliente = self.request.user
        
        # Lógica para la selección automática de empleado
        if not form.cleaned_data['empleado_asignado']:
            # Busca un empleado disponible al azar (o con menos carga, lógica más avanzada aquí)
            empleado_disponible = CustomUser.objects.filter(
                rol='employee',
                empleadoprofile__disponible=True
            ).order_by('?').first() # '?' lo elige al azar
            form.instance.empleado_asignado = empleado_disponible

        self.object = form.save()
        # Aquí podrías añadir un mensaje de éxito con `django.contrib.messages`
        return redirect(self.get_success_url())
    
    
# --- NUEVA VISTA TIPO API ---
def get_empleados_por_sede(request):
    """
    Devuelve un JSON con los empleados de una sede específica.
    Esta vista será llamada por JavaScript.
    """
    sede_id = request.GET.get('sede_id')
    empleados = CustomUser.objects.filter(
        rol='employee', 
        empleado_profile__sede_id=sede_id
    ).select_related('empleado_profile')
    
    data = [{
        'id': emp.id, 
        'nombre': emp.nombre_completo,
        'experiencia': emp.empleado_profile.experiencia,
        'calificacion': f"{emp.empleado_profile.calificacion:.2f}"
    } for emp in empleados]
    
    return JsonResponse(data, safe=False)

