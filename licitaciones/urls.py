from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/nueva/', views.crear_empresa, name='crear_empresa'),
    path('licitacion/nueva/', views.crear_licitacion, name='crear_licitacion'),
    path('licitador/nuevo/', views.crear_licitador, name='crear_licitador'),
    path('oferta/nueva/', views.crear_oferta, name='crear_oferta'),
    path('buscar/', views.buscar_licitacion, name='buscar_licitacion'),
    path('resultados/', views.resultados_busqueda, name='resultados_busqueda'),
    path('licitaciones/', views.listar_licitaciones, name='listar_licitaciones'),
]
