
from django.db import models

class Material(models.Model):
    descripcion = models.CharField(max_length=100,
        null=False, blank=False, unique=True)
    #marca_comercial = models.ForeignKey(MarcaComercial,on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=20, unique=True)
    codigo_barra_imagen = models.ImageField(upload_to='materiales',
        blank=True, null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=10,
        null=True, blank=True)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10,
        null=True, blank=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Materiales"


# Create your models here.
