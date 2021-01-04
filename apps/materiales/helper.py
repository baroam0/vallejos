
from io import BytesIO
from random import randint
from barcode import EAN13, UPCA
from barcode.writer import ImageWriter

from .models import Material


def validarcodigo(parametro):
    try:
        consulta = Material.objects.get(codigo_barra=str(parametro))
        return True
    except:
        return False

def gcb():
    cod = randint(100000000000, 9999999999999)
    valor = validarcodigo(str(cod))
    while valor == True:
        valor = validarcodigo(cod)
    rv = BytesIO()
    EAN13(str(cod), writer=ImageWriter()).write(rv)
    return cod, rv


def generacodigo(cod):
    rv = BytesIO()
    EAN13(str(cod), writer=ImageWriter()).write(rv)
    return rv