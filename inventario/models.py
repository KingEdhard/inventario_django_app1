from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Producto(models.Model):
    # Definición de atributos del modelo
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    marca = models.CharField(max_length=100)
    stock_min = models.IntegerField(validators=[MinValueValidator(1)])
    stock_max = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name.strip()
