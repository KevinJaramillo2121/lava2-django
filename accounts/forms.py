from django import forms
from .models import CustomUser, Vehiculo

class CustomUserCreationForm(forms.ModelForm):
    # Campos para el vehículo
    placa = forms.CharField(max_length=10, label="Placa del Vehículo")
    modelo_vehiculo = forms.CharField(max_length=50, label="Modelo del Vehículo")

    class Meta:
        model = CustomUser
        fields = (
            'documento_identidad',
            'nombre_completo',
            'username',
            'email',
            'fecha_nacimiento',
            'password',  # Se manejará por separado en la vista
        )
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Crear el vehículo asociado al usuario
            Vehiculo.objects.create(
                propietario=user,
                placa=self.cleaned_data['placa'],
                modelo=self.cleaned_data['modelo_vehiculo']
            )
        return user
