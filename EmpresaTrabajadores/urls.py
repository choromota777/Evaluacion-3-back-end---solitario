"""
URL configuration for EmpresaTrabajadores project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include 
from ModelosApp import views as vistas
from django.conf.urls.static import static
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tablaempleados/', vistas.paginaI),
    path('agregar/', vistas.agregarEmpleados),
    path('editar/<int:id>', vistas.editarEmpleados),
    path('eliminar/<int:id>', vistas.eliminarEmpleados),
    path('', include('usuarios.urls', namespace='usuarios')),
    path('tablaempleados/', include('ModelosApp.urls', namespace='ModelosApp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)