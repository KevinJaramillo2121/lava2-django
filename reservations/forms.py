from django import forms
from .models import Reserva, TipoLavado, Producto, Sede
from accounts.models import CustomUser
import datetime

class ReservaForm(forms.ModelForm):
    sede = forms.ModelChoiceField(
        queryset=Sede.objects.all(),
        label="Selecciona una Sede",
        empty_label="Elige dónde quieres tu lavado"
    )
    fecha_cita = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.date.today().isoformat()}),
        label="Día de la cita"
    )
    hora_cita = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Hora de la cita"
    )
    # Campo para seleccionar el empleado
    empleado_asignado = forms.ModelChoiceField(
        queryset=CustomUser.objects.none(),
        required=False, # No es obligatorio para permitir la selección automática
        label="Selecciona un empleado",
        empty_label="Selección automática (cualquier empleado disponible)"
    )

    # Campos para seleccionar productos por categoría
    shampoos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(categoria='shampoo'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Shampoos"
    )
    ceras = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(categoria='cera'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Ceras"
    )
    siliconas = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(categoria='silicona'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Siliconas"
    )
    partes_negras = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(categoria='partes_negras'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cuidado de Partes Negras"
    )
    cuidado_pintura = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.filter(categoria='cuidado_pintura'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cuidado de Pintura"
    )

    class Meta:
        model = Reserva
        fields = ['vehiculo', 'tipo_lavado', 'sede'] 
        widgets = {
            'tipo_lavado': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        # Obtenemos el usuario (cliente) que está haciendo la solicitud
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Filtramos el queryset de vehículos para mostrar solo los del cliente actual
        if user:
            self.fields['vehiculo'].queryset = user.vehiculos.all()

        if 'sede' in self.data:
            try:
                sede_id = int(self.data.get('sede'))
                self.fields['empleado_asignado'].queryset = CustomUser.objects.filter(
                    rol='employee', 
                    empleado_profile__sede_id=sede_id,
                    empleado_profile__disponible=True
                )
            except (ValueError, TypeError):
                pass # Si el ID no es válido, el queryset permanece vacío
        
        self.productos_fields = ['shampoos', 'ceras', 'siliconas', 'partes_negras', 'cuidado_pintura']
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get("fecha_cita")
        hora = cleaned_data.get("hora_cita")

        if fecha and hora:
            cleaned_data['fecha_hora_cita'] = datetime.datetime.combine(fecha, hora)
        
        return cleaned_data
        
        # Juntamos todos los campos de productos en uno solo para validación
        self.productos_fields = ['shampoos', 'ceras', 'siliconas', 'partes_negras', 'cuidado_pintura']
    
    def save(self, commit=True):
        # Obtenemos los productos de todos los campos de seleccion multiple
        productos_seleccionados = []
        for field_name in self.productos_fields:
            productos_seleccionados.extend(self.cleaned_data[field_name])

        # Creamos la instancia de la reserva sin guardarla aun
        reserva = super().save(commit=False)
        
        reserva.fecha_hora_cita = self.cleaned_data['fecha_hora_cita']

        # Calculamos el precio total
        reserva.precio_total = reserva.tipo_lavado.precio
        
        if commit:
            reserva.save()
            # La función `set` es la forma correcta de añadir relaciones ManyToMany
            reserva.productos.set(productos_seleccionados)
        
        return reserva
