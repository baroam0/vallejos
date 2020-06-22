
from django.core.files import File

from apps.materiales.helper import gcb
from apps.materiales.models import Material, MarcaComercial


materiales_archivo = open("materiales.txt", "r")
materiales = materiales_archivo.readlines()

materiales = list(dict.fromkeys(materiales))

marca = MarcaComercial.objects.get(pk=2)


for material in materiales:
    cod, imagen = gcb()
    file_name = str(cod) + ".jpeg"
    imagen = File(imagen, name=file_name)
    m = Material(
        descripcion = str(material),
        marca_comercial = marca,
        codigo_barra = cod,
        codigo_barra_imagen = imagen
    )
    m.save()
    print("Grabando")
