from django.urls import path
from . import views
from .views import acercademi

urlpatterns = [
    path('', views.catalogo_productos, name='catalogo'),
    path('acerca-de-mi/', acercademi, name='acercademi'),
]