from django.contrib import admin

from .models import EmpleadoProfile, TipoLavado, Producto, Reserva

# Registramos los modelos para que aparezcan en el panel de admin
admin.site.register(EmpleadoProfile)
admin.site.register(TipoLavado)
admin.site.register(Producto)
admin.site.register(Reserva)