from django.contrib import admin
from django.utils.html import mark_safe
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('previsualizacion_imagen', 'nombre', 'categoria', 'precio', 'stock', 'marca')
    
    readonly_fields = ('previsualizacion_imagen',)
    
    list_filter = ('categoria', 'marca')
    search_fields = ('nombre',)
    
    def previsualizacion_imagen(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" style="width: 150px; height: 150px; object-fit: cover; border-radius: 8px; border: 1px solid #ccc;" />')
        return "Sin Imagen"
    previsualizacion_imagen.short_description = 'Imagen'