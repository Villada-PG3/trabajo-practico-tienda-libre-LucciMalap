from django.urls import path
from . import views
from .views import acercademi

urlpatterns = [
    path('', views.catalogo_productos, name='home'),
    path('acerca-de-mi/', acercademi, name='acercademi'),
]