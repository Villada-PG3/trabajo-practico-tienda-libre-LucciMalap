from django.shortcuts import render
from .models import Producto, Categoria

def catalogo_productos(request):
    # Obtenemos todas las categorías para mostrar los filtros
    categorias = Categoria.objects.all()
    
    # Revisamos si la URL trae un parámetro de filtro (ej: ?categoria=1)
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        # Filtramos los productos por la categoría seleccionada
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        # Si no hay filtro, mostramos todos
        productos = Producto.objects.all()

    contexto = {
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, 'tiendalibre/catalogo.html', contexto)
def acercademi(request):
    return render(request, 'tiendalibre/acercademi.html')