from django.shortcuts import render
import datetime
from .models import Producto, Categoria

"""def catalogo_productos(request):
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
    return render(request, 'tiendalibre/acercademi.html')"""
from django.shortcuts import render
import datetime

def catalogo_productos(request):
    categorias_lista = [
        {'id': 1, 'nombre': 'Electronica'},
        {'id': 2, 'nombre': 'Hogar'},
        {'id': 3, 'nombre': 'Deportes'},
        {'id': 4, 'nombre': 'Libros'},
        {'id': 5, 'nombre': 'Ropa'}
    ]

    productos_destacados = [
        {
            'nombre': 'zapatillas deportivas runner',
            'descripcion': 'Zapatillas ideales para correr maratones largas y entrenar todos los días en asfalto.',
            'precio': 45000.5,
            'stock': 5,
            'marca': 'Topper',
            'fecha_ingreso': datetime.date(2026, 8, 20),
            'categoria': 'Deportes',
            'imagen': './media/productos/zapatillas.jpeg'
        },
        {
            'nombre': 'REMERA DE ALGODÓN',
            'descripcion': 'Remera básica 100% algodón peinado.',
            'precio': 12000,
            'stock': 10,
            'marca': 'Adidas',
            'fecha_ingreso': datetime.date(2026, 8, 25),
            'categoria': 'Ropa',
            'imagen': './media/productos/remeraAlgodon.jpeg'
        },
        {
            'nombre': 'Auriculares Bluetooth',
            'descripcion': 'Auriculares con cancelación de ruido activa.',
            'precio': None, 
            'stock': 15,
            'marca': 'Daewoo',
            'fecha_ingreso': datetime.date(2026, 8, 30),
            'categoria': 'Electronica',
            'imagen': './media/productos/auriculares.jpeg'
        },
        {
            'nombre': 'Reloj Inteligente Fit',
            'descripcion': 'Mide tus pulsaciones y recibe notificaciones al instante.',
            'precio': 35000,
            'stock': 4,
            'marca': 'Gadnic',
            'fecha_ingreso': datetime.date(2026, 8, 31),
            'categoria': 'Electronica',
            'imagen': './media/productos/Reloj.jpeg'
        },
        {
            'nombre': 'Mochila Urbana Resistente',
            'descripcion': 'Mochila resistente al agua con compartimento para notebook.',
            'precio': 28500.99,
            'stock': 9,
            'marca': 'Gadnic',
            'fecha_ingreso': datetime.date(2026, 8, 15),
            'categoria': 'Deportes',
            'imagen': './media/productos/mochila.jpeg'
        },
        {
            'nombre': 'Termo de Acero Inoxidable',
            'descripcion': 'Conserva el agua caliente por 24 horas continuas sin perder temperatura.',
            'precio': 18000,
            'stock': 5,
            'marca': 'Stanley',
            'fecha_ingreso': datetime.date(2026, 8, 10),
            'categoria': 'Hogar',
            'imagen': './media/productos/termo.jpeg'
        },
        {
            'nombre': 'El hombre en busca de sentido',
            'descripcion': 'Un libro bastante mal presentado en filosofia.',
            'precio': 18000,
            'stock': 0,
            'marca': 'El emporio',
            'fecha_ingreso': datetime.date(2026, 8, 10),
            'categoria': 'Libros',
            'imagen': './media/productos/libro.jpeg'
        }
    ]
    categoria_id = request.GET.get('categoria')

    if categoria_id:
        nombre_cat = None
        for cat in categorias_lista:
            if str(cat['id']) == str(categoria_id):
                nombre_cat = cat['nombre']
                break
        
        if nombre_cat:
            productos_filtrados = []
            for prod in productos_destacados:
                if prod['categoria'] == nombre_cat:
                    productos_filtrados.append(prod)
            
            productos_destacados = productos_filtrados

    context = {
        'productos_destacados': productos_destacados,
        'categorias_lista': categorias_lista,
    }
    
    return render(request, 'tiendalibre/home.html', context)
def acercademi(request):
    return render(request, 'tiendalibre/acercademi.html')