from django.contrib import admin
from Empresita.models import *


class ClienteAdmin(admin.ModelAdmin):
    #Previsualizacion de datos
    list_display = ['nombre', 'telefono', 'rut',]

    #Para buscar mediante palabras claves
    search_fields = ['nombre', 'telefono', 'rut',]

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

class ProductoInline(admin.TabularInline):
    model = Producto

class ProveedorAdmin(admin.ModelAdmin):
    #Previsualizacion de datos
    list_display = ['nombre', 'rut', 'telefono', 'web', 'direccion']

    #Filtro de busqueda
    search_fields = ['nombre', 'rut',]

    inlines = [ProductoInline,]

class VentaAdmin(admin.ModelAdmin):
    #previsualizacion de datos
    list_display = ['cliente', 'producto', 'cantidad', 'descuento', 'precio_final', 'fecha']

    #Para excluir atributos
    exclude = ['monto_final']

    #Para poner o sacar decuentos
    actions = ['desc', 'ndesc']

    def desc(self, request, queryset):
        return queryset.update(descuento = True)
    desc.short_description = 'Con Descuento'

    def ndesc(self, request, queryset):
        return queryset.update(descuento = False)
    ndesc.short_description = 'Sin Descuento'







# Register your models here.
admin.site.register(Venta, VentaAdmin,)
admin.site.register(Cliente, ClienteAdmin,)
admin.site.register(Proveedor, ProveedorAdmin,)
admin.site.register(Producto, ProductoAdmin,)
admin.site.register(Categoria,)
admin.site.register(Direccion,)

