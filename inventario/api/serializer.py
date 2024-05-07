from rest_framework import serializers
from inventario.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    # Le pasamos a la clase anidada Meta las configuraciones iniciales
    class Meta:
        # Primero el modelo
        model = Producto
        # Le indicamos que trabaje con todos los campos del modelo
        fields = '__all__'