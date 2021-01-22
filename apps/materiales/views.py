
from django.contrib import messages
from django.core.files import File
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import MaterialForm, MaterialSinCodigo
from .models import Material

from apps.materiales.helper import gcb, generacodigo


def materialeslistado(request):
    if 'txtBuscar' in request.GET:
        parametro = request.GET.get('txtBuscar')
        consulta = Material.objects.filter(
            Q(descripcion__icontains=parametro) |
            Q(codigo_barra__icontains=parametro)
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
            consulta = Material.objects.latest("pk")
            consulta.codigo_barra_imagen = generacodigo(consulta.codigo_barra)
            file_name = str(consulta.codigo_barra) + ".jpeg"
            imagen = File(consulta.codigo_barra_imagen, name=file_name)
            consulta.codigo_barra_imagen = imagen
            consulta.save()

            messages.success(request, "SE HA GRABADO EL MATERIAL")
            return redirect('/materialeslistado')
        else:
            return render(request, 'materiales/material_edit.html', {"form": form})
    else:
        form = MaterialForm()
        return render(request, 'materiales/material_edit.html', {"form": form})


def materialnuevosincodigo(request):
    if request.POST:
        form = MaterialSinCodigo(request.POST)
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
        form = MaterialSinCodigo()
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

"""
def ajaxmaterial(request):
    parametro = request.GET.get('txtBuscarterm')
    material = Material.objects.filter(descripcion__icontains=parametro)

    dict_tmp = dict()
    list_tmp = list()

    if len(material) > 0:
        for i in material:
            dict_tmp["id"] = i.pk
            dict_tmp["text"] = i.descripcion.upper()
            list_tmp.append(dict_tmp)
            dict_tmp = dict()

    return JsonResponse(list_tmp, safe=False)
"""


# Create your views here.
