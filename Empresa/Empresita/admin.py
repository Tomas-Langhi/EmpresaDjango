from django.contrib import admin
from Empresita.models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'rut',]

class ProductoAdmin(admin.ModelAdmin):
    #Para armar pestañas separando los datos
    fieldsets = (
        ('Descripción',{
            'fields': ('nombre',)
        }),
        ('Variables',{
            'fields': ('precio', 'stock',)
        }),
    )




# Register your models here.
admin.site.register(Cliente, ClienteAdmin,)
admin.site.register(Proveedor,)
admin.site.register(Producto, ProductoAdmin,)
admin.site.register(Categoria,)
admin.site.register(Venta,)
admin.site.register(Direccion,)

