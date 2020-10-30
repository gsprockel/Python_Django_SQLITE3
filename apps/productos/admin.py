from django.contrib import admin

# Register your models here.
from apps.productos.models import tipoProducto, Producto

admin.site.register(tipoProducto)
admin.site.register(Producto)
