from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'fecha')
    list_filter = ('categoria', 'fecha')
    
    search_fields = ('nombre',)
    # También borramos la línea "autocomplete_fields" que era para el autor