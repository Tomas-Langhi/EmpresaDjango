from django.db import models

# Create your models here.

class Direccion(models.Model):
    numero = models.IntegerField(null=True)
    calle = models.CharField(max_length = 50, default="")
    comuna = models.CharField(max_length = 50, default="")
    ciudad = models.CharField(max_length = 50, default="")
    def __str__(self):
        return str(self.ciudad)

class Proveedor(models.Model):
    nombre = models.CharField(max_length = 50, default="")
    telefono = models.IntegerField(null=True)
    web = models.CharField(max_length = 50, default="")
    rut = models.IntegerField(null=False,  unique=True)
    direccion = models.ForeignKey('Direccion', default = None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length = 50, default = "")
    precio = models.FloatField(null = True)
    stock = models.IntegerField(null = True)
    categoria = models.ForeignKey('Categoria', default = None, on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', default = None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)        

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default="")
    telefono = models.IntegerField(null = True)
    rut = models.IntegerField(null = False, unique = True) 
    direccion = models.ForeignKey('Direccion', default = None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Venta(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey('Cliente', default = None, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', default = None, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    descuento = models.BooleanField(null=True)
    monto_final = models.FloatField(null = True)

    def __str__(self):
        return str(self.producto) + " Stock = " + str(self.cantidad)
    
    #Para calcular el monto final
    def precio_final(self):
        self.monto_final =  self.producto.precio * self.cantidad
        return self.monto_final
    precio_final.short_description = 'Precio Final'
