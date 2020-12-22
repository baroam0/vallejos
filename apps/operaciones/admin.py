from django.contrib import admin

<<<<<<< HEAD
from .models import Operacion

admin.site.register(Operacion)
=======
from .models import Operacion, DetalleOperacion

admin.site.register(Operacion)
admin.site.register(DetalleOperacion)
>>>>>>> 01535ddc6a6a45457e8953af93623cf4a3ddabfd

# Register your models here.
