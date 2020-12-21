
from django import forms

from .models import DetalleOperacion
from apps.materiales.models import Material


class DetalleOperacionForm(forms.ModelForm):
    material = forms.ModelChoiceField(
        label="Material",
        queryset=Material.objects.all()
        )
    cantidad = forms.DecimalField(
        label="Cantidad",
        required=True
    )
    precio = forms.DecimalField(
        label="Precio",
        required=True
    )

    class Meta:
        model = DetalleOperacion
        fields = ['material', 'cantidad', 'precio']
