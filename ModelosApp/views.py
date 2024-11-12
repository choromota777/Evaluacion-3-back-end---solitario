from django.shortcuts import render, redirect
from django.http import HttpResponse
from  ModelosApp.models import Employee
from ModelosApp.forms import FormularioEmpleados
# Create your views here.

def paginaI(request):
    empleados = Employee.objects.all()
    data= {'empleados':empleados}
    return render(request, "base.html", data)

def agregarEmpleados(request):
    form = FormularioEmpleados(request.POST)
    if(form.is_valid()):
        form.save()
        return redirect('/')
    data = {'form': form, 'titulo':'Agregar'}
    return render(request, 'agregar.html', data)

def editarEmpleados(request, id):
    empleado = Employee.objects.get(id = id)
    form = FormularioEmpleados(instance=empleado)
    if(request.method == 'POST'):
        form = FormularioEmpleados(request.POST, instance=empleado)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    data = {'form': form, 'titulo': 'Editar'}
    return render(request, 'agregar.html', data)


def eliminarEmpleados(request, id):
    empleado = Employee.objects.get(id = id)
    empleado.delete()
    return redirect('/')