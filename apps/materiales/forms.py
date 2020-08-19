

from django import forms
from .models import MarcaComercial, Material


class MaterialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    marca_comercial = forms.ModelChoiceField(
        queryset=MarcaComercial.objects.all(),
        label="Descripcion",
        required=True
        )
    precio = forms.DecimalField(label="Precio", required=True)

    class Meta:
        model = Material
        fields = ['descripcion', 'marca_comercial', 'precio']


class MarcaComercialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)

    class Meta:
        model = MarcaComercial
        fields = ['descripcion']

