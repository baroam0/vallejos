

from django import forms
from .models import MarcaComercial


class MarcaComercialForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripcion", required=True)

    class Meta:
        model = MarcaComercial
        fields = ['descripcion']

