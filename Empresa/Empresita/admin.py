from django.contrib import admin
from Empresita.models import *


class ClienteAdmin(admin.ModelAdmin):
    #Previsualizacion de datos
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
        ('Detalles',{
            'fields': ('proveedor', 'categoria',)
        }),
    )

class ProveedorAdmin(admin.ModelAdmin):
    #Previsualizacion de datos
    list_display = ['nombre', 'rut', 'telefono', 'web', 'direccion']

    #Filtro de busqueda
    search_fields = ['nombre', 'rut',]

class VentaAdmin(admin.ModelAdmin):
    #previsualizacion de datos
    list_display = ['cliente', 'producto', 'cantidad', 'desc', 'precio_final', 'fecha']

    #Para excluir atributos
    exclude = ['monto_final']




# Register your models here.
admin.site.register(Venta, VentaAdmin,)
admin.site.register(Cliente, ClienteAdmin,)
admin.site.register(Proveedor, ProveedorAdmin,)
admin.site.register(Producto, ProductoAdmin,)
admin.site.register(Categoria,)
admin.site.register(Direccion,)

