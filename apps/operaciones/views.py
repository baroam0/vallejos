
from django.shortcuts import render

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
