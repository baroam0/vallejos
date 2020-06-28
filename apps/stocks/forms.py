
from django import forms 

from apps.complementos_generales.models import Unidad
from apps.materiales.models import Material, MarcaComercial
from .models import Stock


class StockForm(forms.ModelForm):
    material = forms.ModelChoiceField(
        label="Material", queryset=Material.objects.all(), required=True)
    unidad = forms.ModelChoiceField(label="Unidad", queryset=Unidad.objects.all())
    cantidad = forms.DecimalField(label="Cantidad", required=True)

    class Meta:
        model = Stock
        fields = ["material", "unidad", "cantidad"]
