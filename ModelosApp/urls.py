from django.urls import path
from . import views

app_name = 'ModelosApp'

urlpatterns = [
    path('tabla/', views.paginaI, name='paginaI'),  # Añadimos la ruta para la tabla de usuarios
    path('agregar/', views.agregarEmpleados, name='agregarEmpleado'),  # Para agregar empleados
    path('editar/<int:id>/', views.editarEmpleados, name='editarEmpleado'),  # Para editar empleados
    path('eliminar/<int:id>/', views.eliminarEmpleados, name='eliminarEmpleado'),  # Para eliminar empleados
]
