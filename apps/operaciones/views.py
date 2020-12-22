
<<<<<<< HEAD
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
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
    resultados = DetalleOperacion.objects.filter(operacion=pk)
    return render(
        request,
        'operaciones/operacion_edit.html',
        {
            "resultados": resultados
        })


def ajaxconsultamaterial(request):
    codigobarra = request.GET.get("codigo")
    cantidad = request.GET.get("cantidad")
    
    material = Material.objects.get(codigo_barra=codigobarra)
    subtotal = float(cantidad) * float(material.precio)
    operacion = Operacion.objects.create(fecha=datetime.now())
    operacion.save()
    operacion = Operacion.objects.latest("pk")
    detalleoperacion = DetalleOperacion.objects.create(
        operacion = operacion,
        material = material,
        cantidad = cantidad,
        precio = subtotal,
    )

    detalleoperacion.save

    response = {
        'pk': operacion.pk,
    }
    return JsonResponse(response)

=======
from django.shortcuts import render
>>>>>>> 01535ddc6a6a45457e8953af93623cf4a3ddabfd

from django.core.paginator import Paginator

from .models import Operacion, DetalleOperacion

def operacionlistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Operacion.objects.filter(
            Q(descripcion__icontains=parametro) |
            Q(marca_comercial__descripcion__icontains=parametro)
        ).order_by('descripcion')
    else:
        consulta = Operacion.objects.all().order_by('fecha')
    paginador = Paginator(consulta, 25)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'operaciones/operacion_list.html', {'resultados': resultados})


# Create your views here.
