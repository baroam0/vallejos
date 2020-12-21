
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Operacion, DetalleOperacion
from apps.materiales.models import Material


def operacionlistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Operacion.objects.filter(fecha=parametro).order_by('fecha')
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
        'operaciones/operacion_nueva.html',
    )


def operacioneditar(request, pk):
    return render(request, 'operaciones/operacion_nueva.html')


def ajaxconsultamaterial(request):
    codigobarra = request.GET.get("codigo")
    material = Material.objects.get(codigo_barra=codigobarra)

    response = {
        'material': material.descripcion,
        'precio': material.precio
    }
    return JsonResponse(response)


# Create your views here.
