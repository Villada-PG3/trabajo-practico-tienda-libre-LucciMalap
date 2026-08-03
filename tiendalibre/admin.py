from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto
admin.site.register(Producto)
admin.site.site_header = "Tienda Libre Admin"
admin.site.site_title = "Tienda Libre Admin Portal"
admin.site.index_title = "Welcome to Tienda Libre Admin Portal"
admin.site.register(Categoria)