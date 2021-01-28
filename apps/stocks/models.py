

from django.db import models

from apps.complementos_generales.models import Unidad
from apps.materiales.models import Material


class Stock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.material) + " - " + str(self.cantidad)

    class Meta:
        verbose_name_plural = "Stocks"
        unique_together = ('material','unidad')


# Create your models here.
