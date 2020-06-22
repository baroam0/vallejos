
from django.db import models


class MarcaComercial(models.Model):
    descripcion = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Marcas Comerciales"


class Material(models.Model):
    descripcion = models.CharField(max_length=100,
        null=False, blank=False, unique=True)
    marca_comercial = models.ForeignKey(MarcaComercial,
        on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=20, unique=True)
    codigo_barra_imagen = models.ImageField(upload_to='materiales',
        blank=True)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Materiales"



# Create your models here.
