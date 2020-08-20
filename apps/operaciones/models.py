
from django.db import models
from apps.materiales.models import Material


class Operacion(models.Model):
    fecha = models.DateTimeField()
    cliente = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.fecha)
    
    @property
    def total(self):
        operaciones = DetalleOperacion.objects.filter(operacion=self.pk)
        total = 0
        for op in operaciones:
            producto = op.cantidad * op.precio
            total = total + producto
        return total

    class Meta:
        verbose_name_plural = "Operaciones"


class DetalleOperacion(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE)
    mercaderia = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10,
        null=False, blank=False)
    precio = models.DecimalField(decimal_places=2, max_digits=10,
        null=False, blank=False)

    def __str__(self):
        return str(self.operacion)

    class Meta:
        verbose_name_plural = "Detalles Operaciones"



# Create your models here.
