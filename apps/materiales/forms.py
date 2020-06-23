

from django import forms
from .models import MarcaComercial, Material


class MaterialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)
    marca_comercial = forms.ModelChoiceField(
        queryset=MarcaComercial.objects.all(),
        label="Descripcion",
        required=True
        )

    class Meta:
        model = Material
        fields = ['descripcion', 'marca_comercial']


class MarcaComercialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)

    class Meta:
        model = MarcaComercial
        fields = ['descripcion']

