

from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    codigo_barra = forms.CharField(label="Codigo Barra", required=True)
    precio = forms.DecimalField(label="Precio", required=True)
    cantidad = forms.DecimalField(label="Cantidad", required=True)

    class Meta:
        model = Material
        fields = ['descripcion', 'codigo_barra', 'precio', 'cantidad']


class MaterialSinCodigo(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    precio = forms.DecimalField(label="Precio", required=True)
    cantidad = forms.DecimalField(label="Cantidad", required=True)

    class Meta:
        model = Material
        fields = ['descripcion', 'precio', 'cantidad']
