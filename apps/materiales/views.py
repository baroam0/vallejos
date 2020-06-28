
from django.contrib import messages
from django.core.files import File
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import MarcaComercialForm, MaterialForm
from .models import Material, MarcaComercial

from apps.materiales.helper import gcb


def materialeslistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Material.objects.filter(
            Q(descripcion__icontains=parametro) |
            Q(marca_comercial__descripcion__icontains=parametro)
        ).order_by('descripcion')
    else:
        consulta = Material.objects.all().order_by('descripcion')
    paginador = Paginator(consulta, 25)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'materiales/material_list.html', {'resultados': resultados})


def materialnuevo(request):
    if request.POST:
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            cod, imagen = gcb()
            file_name = str(cod) + ".jpeg"
            imagen = File(imagen, name=file_name)

            consulta = Material.objects.latest("pk")
            consulta.codigo_barra = cod
            consulta.codigo_barra_imagen = imagen
            consulta.save()
            
            messages.success(request, "SE HA GRABADO EL MATERIAL")
            return redirect('/materialeslistado')
        else:
            return render(request, 'materiales/material_edit.html', {"form": form})
    else:
        form = MaterialForm()
        return render(request, 'materiales/material_edit.html', {"form": form})


def materialeditar(request, pk):
    consulta = Material.objects.get(pk=pk)
    if request.POST:
        form = MaterialForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO EL MATERIAL")
            return redirect('/materialeslistado')
        else:
            return render(request, 'materiales/material_edit.html', {"form": form})
    else:
        form = MaterialForm(instance=consulta)
        return render(request,
            'materiales/material_edit.html',
            {"form": form}
        )


#############################################################################
############################ SECCION MARCA COMERCIAL ########################
#############################################################################


def marcacomerciallistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = MarcaComercial.objects.filter(
            descripcion__icontains=parametro
        ).order_by('descripcion')
    else:
        consulta = MarcaComercial.objects.all().order_by('descripcion')
    paginador = Paginator(consulta, 25)
    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(
        request,
        'materiales/marcacomercial_list.html',
        {'resultados': resultados})


def marcacomercialnueva(request):
    if request.POST:
        form = MarcaComercialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO LA MARCA COMERCIAL")
            return redirect('/marcacomerciallistado')
        else:
            return render(request, 'materiales/material_edit.html', {"form": form})
    else:
        form = MarcaComercialForm()
        return render(request, 'materiales/marcacomercial_edit.html', {"form": form})


def marcacomercialeditar(request, pk):
    consulta = MarcaComercial.objects.get(pk=pk)
    if request.POST:
        form = MarcaComercialForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO LA MARCA COMERCIAL")
            return redirect('/marcacomerciallistado')
        else:
            return render(request, 'materiales/marcacomercial_edit.html', {"form": form})
    else:
        form = MarcaComercialForm(instance=consulta)
        return render(request, 'materiales/marcacomercial_edit.html', {"form": form})



# Create your views here.
