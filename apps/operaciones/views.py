
import json
from datetime import datetime

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render


from .models import Operacion, DetalleOperacion
from apps.materiales.models import Material


def operacionlistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Operacion.objects.filter(
            fecha=parametro
        ).order_by('fecha')
    else:
        consulta = Operacion.objects.all().order_by('fecha')
    paginador = Paginator(consulta, 25)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'operaciones/operacion_list.html', {'resultados': resultados})


def operacionnueva(request):
    return render(
        request,
        "operaciones/operacion_nueva.html"
    )


def operacioneditar(request,pk):
    resultados = DetalleOperacion.objects.filter(operacion=pk)

    return render(
        request,
        "operaciones/operacion_edit.html",
        {
            "resultados": resultados
        }
    )


def ajaxmaterial(request):
    codigo = request.GET.get("codigo")
    cantidad = request.GET.get("cantidad")

    try:
        material = Material.objects.get(codigo_barra=codigo)
        subtotal = round(float(material.precio) * float(cantidad),2)
        datos = {
            "status": 200,
            "pk": material.pk,
            "descripcion": material.descripcion.upper(),
            "cantidad": cantidad,
            "precio": material.precio,
            "subtotal": subtotal
            }

        return JsonResponse(datos)
    except Material.DoesNotExist:
        datos = {"status": 404}
        return JsonResponse(datos)


def ajaxguardaroperacion(request):
    data = request.POST["datos"]
    dd = json.dumps(data)
    print(dd)


# Create your views here.
