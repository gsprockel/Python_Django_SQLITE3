from django.db import models

# Create your models here.
class tipoProducto(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    precio = models.FloatField()
    stockmin = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    tipo_producto = models.ForeignKey(tipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

