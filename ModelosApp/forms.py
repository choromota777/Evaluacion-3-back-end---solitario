from django import forms
from django.core import validators
from ModelosApp.models import Employee
import re 

# Validador para el formato RUT
def validar_rut(value):
    if not re.match(r'^\d{7,8}-[0-9kK]$', value):
        raise forms.ValidationError("El RUT debe tener el formato XXXXXXXX-X, incluyendo el guión y dígito verificador.")

class FormularioEmpleados(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    nombre = forms.CharField(label='Nombre Empleados', required=True)    
    email = forms.CharField(label='Email', required=False)
    telefono = forms.CharField(label='Telefono', required=False, validators=[validators.MinLengthValidator(9), validators.MaxLengthValidator(12)])
    rut = forms.CharField(label='RUT', required=True, validators=[validar_rut])  
    # Agregar clases CSS a cada campo
    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control' 