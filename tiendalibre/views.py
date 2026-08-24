from django.shortcuts import render
from .models import Producto, Categoria

def catalogo_productos(request):
    categorias = Categoria.objects.all()
    
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    contexto = {
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, 'tiendalibre/catalogo.html', contexto)
def acercademi(request):
    return render(request, 'tiendalibre/acercademi.html')