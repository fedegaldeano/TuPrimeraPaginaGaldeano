from django import forms
from .models import EmpresaLicitante, Licitacion, Licitador, Oferta

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = EmpresaLicitante
        fields = '__all__'

class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = '__all__'

class LicitadorForm(forms.ModelForm):
    class Meta:
        model = Licitador
        fields = '__all__'

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['licitador', 'licitacion', 'propuesta_tecnica', 'propuesta_economica']

class BuscarLicitacionForm(forms.Form):
    titulo = forms.CharField(label='Buscar licitación por título', max_length=100)
