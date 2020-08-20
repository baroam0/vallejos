from django.contrib import admin

from .models import Operacion, DetalleOperacion

admin.site.register(Operacion)
admin.site.register(DetalleOperacion)

# Register your models here.
