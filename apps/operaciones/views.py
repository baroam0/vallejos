

from datetime import datetime
from django.db.models import Q, Sum
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.complementos_generales.models import Unidad
from apps.materiales.models import Material
from apps.operaciones.models import Operacion, DetalleOperacion
from apps.stocks.models import Stock

from apps.libs.funcionfecha import revertirfecha


def ajaxconsultamaterial(request):
    try:
        codigobarra = request.GET.get("codigobarra")
        cantidad = request.GET.get("cantidad")
        material = Material.objects.get(codigo_barra=codigobarra)
        stock = Stock.objects.get(material=material)
        preciosubtotal = float(material.precio) * float(cantidad)
        data ={
            "materialid": material.pk,
            "material": material.descripcion.upper(),
            "cantidad": cantidad,
            "precio": material.precio,
            "unidad": stock.unidad.descripcion,
            "subtotal": preciosubtotal,
            "error": 0
        }
    except:
        data = {
            "error": 1
        }

    return JsonResponse(data, safe=False)


def operacionlistado(request):
    resultados = None
    if "txtBuscar" in request.GET:
        parametro = request.GET.get("txtBuscar")
        if parametro!="":
            if parametro.isnumeric():
                try:
                    resultados = DetalleOperacion.objects.get(
                        pk=int(parametro)
                    )
                except:
                    resultados=None
            else:
                resultados = DetalleOperacion.objects.filter(
                    Q(obra__descripcion__icontains=parametro) |
                    Q(contratista__descripcion__icontains=parametro)).order_by("fecha")
        else:
            resultados = Operacion.objects.all().values('').annotate()

    return render(
        request,
        "operaciones/operacion_list.html",
        {
            "resultados": resultados
        }
    )


def operacionnueva(request):
    return render(
        request,
        "operaciones/operacion_nueva.html",
    )


@csrf_exempt
def ajaxgrabaroperacion(request):
    fecha = datetime.today()

    vectormateriales=request.POST.getlist('vectormateriales[]')
    vectorcantidades=request.POST.getlist('vectorcantidades[]')
    vectorunidades=request.POST.getlist('vectorunidades[]')
    vectorprecios=request.POST.getlist('vectorprecios[]')

    vectormateriales, vectorcantidades, vectorcantidades

    operacion = Operacion(
        fecha=fecha
    )

    operacion.save()
    operacion = Operacion.objects.latest("pk")

    for (material, unidad, cantidad, precio) in zip(vectormateriales, vectorunidades, vectorcantidades, vectorprecios):
        material = Material.objects.get(pk=int(material))

        detalleoperacion = DetalleOperacion(
            operacion=operacion,
            material=material,
            cantidad=cantidad,
            precio_unitario=precio,
            precio_subtotal= float(cantidad)*float(precio)
        )

        detalleoperacion.save()

    data = {
        "status": 200
    }
    return JsonResponse(data)


def operacioneditar(request, pk):
    contratistas = Contratista.objects.all()
    unidades = Unidad.objects.all().order_by("descripcion")
    obras = Obra.objects.all().order_by("descripcion")

    orden = Orden.objects.get(pk=pk)
    detallesorden = DetalleOrden.objects.filter(
        orden=orden
    )

    return render(
        request,
        "ordenes/orden_edit.html",
        {
            "orden": orden,
            "detallesorden": detallesorden,
            "contratistas": contratistas,
            "unidades": unidades,
            "obras": obras
        }
    )


@csrf_exempt
def ajaxgrabareditarorden(request,pk):
    detalleorden=DetalleOrden.objects.filter(orden=pk)
    detalleorden.delete()

    fecha = request.POST["fecha"]
    fecha = revertirfecha(fecha)
    contratista= Contratista.objects.get(pk=int(request.POST["contratista"]))
    encargado = request.POST["encargado"]
    obra = Obra.objects.get(pk=int(request.POST["obra"]))

    arraymaterial = request.POST.getlist('arraymaterial[]')
    arrayunidad = request.POST.getlist('arrayunidad[]')
    arraycantidad = request.POST.getlist('arraycantidad[]')

    orden = Orden.objects.get(pk=pk)

    orden = Orden.objects.filter(pk=pk).update(
        fecha=fecha,
        contratista=contratista,
        encargado=encargado,
        obra=obra
    )
    obra.save()

    orden = Orden.objects.get(pk=pk)

    for (material, unidad, cantidad) in zip(arraymaterial, arrayunidad, arraycantidad):
        material = Material.objects.get(pk=int(material))
        unidad = Unidad.objects.get(pk=int(unidad))

        detalleorden = DetalleOrden(
            orden=orden,
            material=material,
            cantidad=cantidad,
            unidad=unidad
        )

        detalleorden.save()

    data = {
        "status": 200
    }

    return JsonResponse(data)


def imprimirorden(request,pk):
    orden = Orden.objects.get(pk=pk)
    detallesorden = DetalleOrden.objects.filter(orden=orden)

    return render(
        request,
        "ordenes/imprimirorden.html",
        {
            "orden": orden,
            "detallesorden": detallesorden
        }
    )

# Create your views here.
