from django.db import models

from apps.complementos_generales.models import Unidad
from apps.materiales.models import Material


class Stock(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.material) + "-" + str(self.cantidad)
    
    class Meta:
        verbose_namme_plural = "Stocks"


# Create your models here.
