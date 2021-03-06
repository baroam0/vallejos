
from django.db import models
from apps.materiales.models import Material


class Operacion(models.Model):
    fecha = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.fecha)

    class Meta:
        verbose_name_plural = "Operaciones"


class DetalleOperacion(models.Model):
    operacion = models.ForeignKey(
        Operacion, null=False, blank=False, on_delete=models.CASCADE)
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=False, blank=False)
    cantidad = models.DecimalField(
        decimal_places=2, max_digits=10, null=False, blank=False)
    precio_unitario = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    precio_subtotal = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    
    def subtotal(self):
        resultado = self.cantidad * self.precio
        return round(resultado,2)

    def __str__(self):
        return str(self.operacion)

    class Meta:
        verbose_name_plural = "Detalles Operaciones"


# Create your models here.
