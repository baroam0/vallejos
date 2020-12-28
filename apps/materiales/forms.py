

from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    codigo_barra = forms.CharField(label="Codigo Barra", required=True)
    precio = forms.DecimalField(label="Precio", required=True)

    class Meta:
        model = Material
        fields = ['descripcion', 'codigo_barra', 'precio']


class MaterialSinCodigo(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    precio = forms.DecimalField(label="Precio", required=True)

    class Meta:
        model = Material
        fields = ['descripcion', 'precio']
