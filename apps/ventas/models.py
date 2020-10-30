from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=25)
    cedula = models.IntegerField()
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=25)
    correo = models.CharField(max_length=35)
    direccion = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class venta(models.Model):
    fecha = models.DateTimeField()
    subtotal = models.FloatField(default=0)
    impuesto = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)


    

