# Consultas de Base de Datos (Django ORM) - Tienda Libre

**1. Obtener todos los productos del catalogo:**
# Producto.objects.all()

**2. Obtener todas las categorias del catalogo:**
# Categoria.objects.all()

**3. Obtener todos los productos de una categoria especifica:**
# categoria = Categoria.objects.get(nombre='Nombre de la Categoria')

**4. Obtener un producto especifico por su ID:**
# producto = Producto.objetcs.get(id=1)

**5. filtrar objetos que tengan stock de mayor a menor:**
# producto = Producto.objects.filter(stock__gt=0)

**6. obtener un producto por su nombre (ignorando mayusculas):**
# producto = Producto.objects.get(nombre__icontains='reloj')

**7. obtener todos los prodcutos ordenados por precio de mayor a menor:**
# producto = Producto.objects.all().order_by('-precio')

**8. obtener todos los productos ordenados por precio de menor a mayor:**
# producto = Producto.objects.all().order_by('precio')

**9. obtener un conteo de todos los prodcutos del sistema:**
# producto = Producto.objects.count()

**10.obtener un conteo de todas las categorias del sistema:**
# categoria = Categoria.objects.count()