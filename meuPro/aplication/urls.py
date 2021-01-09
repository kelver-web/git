from django.urls import path
from aplication import views
from .views import Create

urlpatterns = [
    path('index/', views.index, name='index'),
    path('moda/', views.moda, name='moda'),
    path('beleza/', views.beleza, name='beleza'),
    path('tendencia/', views.tendencia, name='tendencia'),
    path('contato/', Create.as_view(), name='contato'),
    path('unhas/', views.unhas, name='unhas'),
    path('cabelo/', views.cabelo, name='cabelo'),
    path('verao/', views.verao, name='verao'),
    path('inverno/', views.inverno, name='inverno'),
    path('modapraia/', views.modapraia, name='modapraia'),
    path('skincare/', views.skincare, name='skincare'),
    path('corpo/', views.corpo, name='corpo'),   
]
