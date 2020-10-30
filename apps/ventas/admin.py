from django.contrib import admin

# Register your models here.

from apps.ventas.models import cliente, venta

admin.site.register(cliente)
admin.site.register(venta)
