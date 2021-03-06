"""vallejos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import home

from apps.materiales.views import marcacomercialeditar, \
    materialeslistado, materialnuevo, materialeditar, \
    marcacomerciallistado, marcacomercialnueva, materialnuevosincodigo

from apps.stocks.views import stocklistado, stocknuevo, stockeditar

from apps.operaciones.views import (ajaxconsultamaterial, ajaxgrabaroperacion, operacioneditar,
    operacionlistado, operacionnueva)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('materialeslistado/', materialeslistado),
    path('materialnuevosincodigo/', materialnuevosincodigo),
    path('materialnuevo/', materialnuevo),
    path('materialeditar/<int:pk>', materialeditar),
    path('marcacomerciallistado/', marcacomerciallistado),
    path('marcacomercialnueva/', marcacomercialnueva),
    path('marcacomercialeditar/<int:pk>', marcacomercialeditar),
    path('operacionlistado/', operacionlistado),
    path('operacionnueva/', operacionnueva),
    path('operacioneditar/<int:pk>', operacioneditar),
    path('stocklistado/', stocklistado),
    path('stocknuevo/', stocknuevo),
    path('stockeditar/<int:pk>', stockeditar),

    path('ajaxconsultamaterial/', ajaxconsultamaterial),

    #path('ajaxmaterial/', ajaxmaterial),
    path('ajaxgrabaroperacion/', ajaxgrabaroperacion),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

