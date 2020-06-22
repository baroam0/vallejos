from django.db import models


class Unidad(models.Model):
    descripcion = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.descripcion.upper()
    
    class Meta:
        verbose_name_plural = "Undades"
    


# Create your models here.
