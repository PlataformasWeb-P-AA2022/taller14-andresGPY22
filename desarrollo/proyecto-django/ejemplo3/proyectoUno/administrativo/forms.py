from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Departamento, Propietario

class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'edad', 'nacionalidad']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese apellido por favor'),
            'edad': _('Ingrese la edad por favor'),
            'nacionalidad': _('Ingrese la nacionalidad por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        valor = "René"
        ["René"] # 1
        len( ["René"])
        """

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_edad(self):
        valor = self.cleaned_data['edad']
        return valor

    def clean_nacionalidad(self):
        valor = self.cleaned_data['nacionalidad']
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['costo', 'cuartos', 'banios', 'alicuota', 'propietario']


class DepartamentoPropietarioForm(ModelForm):

    def __init__(self, propietario, *args, **kwargs):
        super(DepartamentoPropietarioForm, self).__init__(*args, **kwargs)
        self.initial['propietario'] = propietario
        self.fields["propietario"].widget = forms.widgets.HiddenInput()
        print(propietario)

    class Meta:
        model = Departamento
        fields = ['costo', 'cuartos', 'banios', 'alicuota', 'propietario']
