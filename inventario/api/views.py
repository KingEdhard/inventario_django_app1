# Importamos las vistas desde rest_framework
from rest_framework import viewsets
# Importamos la clase Producto desde el modelo
from inventario.models import Producto
# Importamos desde inventario/api/serializer el Serializer ProductoSerailizer
from inventario.api.serializer import ProductoSerializer

# Creamos la la clase para la vista

class ProductoViewSet(viewsets.ModelViewSet):
    # A toda vista, debemos pasarle un queryset
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
