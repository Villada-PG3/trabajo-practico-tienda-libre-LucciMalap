from django.contrib import admin
from django.utils.html import mark_safe # Importante para renderizar HTML seguro
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # 1. Definimos las columnas a mostrar en la lista del Admin (incluyendo la vista previa)
    list_display = ('previsualizacion_imagen', 'nombre', 'categoria', 'precio', 'stock', 'marca')
    
    # 2. Hacemos que la previsualización también aparezca al editar un producto individual
    readonly_fields = ('previsualizacion_imagen',)
    
    list_filter = ('categoria', 'marca')
    search_fields = ('nombre',)

    # 3. Función que genera la etiqueta <img> en HTML para mostrar la foto
    def previsualizacion_imagen(self, obj):
        if obj.imagen:
            # Cambiamos width y height a 150px (puedes poner el número que quieras)
            return mark_safe(f'<img src="{obj.imagen.url}" style="width: 150px; height: 150px; object-fit: cover; border-radius: 8px; border: 1px solid #ccc;" />')
        return "Sin Imagen"

    # Cambiamos el título que tendrá la columna en la tabla del panel de admin
    previsualizacion_imagen.short_description = 'Imagen'