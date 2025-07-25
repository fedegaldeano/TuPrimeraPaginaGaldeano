from django.shortcuts import render, redirect
from .forms import EmpresaForm, LicitacionForm, LicitadorForm, OfertaForm, BuscarLicitacionForm
from .models import Licitacion
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'licencias/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

@login_required
def profile(request):
    return render(request, 'licencias/profile.html')

def home(request):
    return render(request, 'licencias/home.html')

def crear_empresa(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'licencias/empresa_form.html', {'form': form})

def crear_licitacion(request):
    form = LicitacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'licencias/licitacion_form.html', {'form': form})

def crear_licitador(request):
    form = LicitadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'licencias/licitador_form.html', {'form': form})

def crear_oferta(request):
    form = OfertaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'licencias/oferta_form.html', {'form': form})

def buscar_licitacion(request):
    form = BuscarLicitacionForm()
    return render(request, 'licencias/buscar_licitacion.html', {'form': form})

def resultados_busqueda(request):
    if request.GET.get("titulo"):
        titulo = request.GET["titulo"]
        resultados = Licitacion.objects.filter(titulo__icontains=titulo)
        return render(request, "licencias/licitacion_list.html", {"resultados": resultados})
    else:
        return render(request, "licencias/licitacion_list.html", {"resultados": []})

def listar_licitaciones(request):
    licitaciones = Licitacion.objects.all()
    return render(request, 'licencias/licitacion_list.html', {'resultados': licitaciones})

def about(request):
    return render(request, 'licencias/about.html')
