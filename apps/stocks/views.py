
from django.contrib import messages
from django.core.files import File
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import StockForm
from .models import Stock


def stocklistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Stock.objects.filter(
            material__icontains=parametro
        ).order_by('material')
    else:
        consulta = Stock.objects.all().order_by('material')
    paginador = Paginator(consulta, 25)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'stocks/stock_list.html', {'resultados': resultados})


def stocknuevo(request):
    if request.POST:
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()    
            messages.success(request, "SE HA GRABADO EL STOCK")
            return redirect('/stocklistado')
        else:
            return render(request, 'stocks/stock_edit.html', {"form": form})
    else:
        form = StockForm()
        return render(request, 'stocks/stock_edit.html', {"form": form})


def stockeditar(request, pk):
    consulta = Stock.objects.get(pk=pk)
    if request.POST:
        form = StockForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO EL STOCK")
            return redirect('/stocklistado')
        else:
            return render(request, 'stocks/stock_edit.html', {"form": form})
    else:
        form = StockForm(instance=consulta)
        return render(request,
            'stocks/stock_edit.html',
            {"form": form}
        )


# Create your views here.
