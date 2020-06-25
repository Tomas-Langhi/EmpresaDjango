from django.db import models

# Create your models here.

class Direccion(models.Model):
    Numero = models.CharField(max_length = 50, default="")
    calle = models.IntegerField(null=True)
    comuna = models.CharField(max_length = 50, default="")
    ciudad = models.CharField(max_length = 50, default="")

class Proveedor(models.Model):
    nombre = models.CharField(max_length = 50, default="")
    telefono = models.IntegerField(null=True)
    web = models.CharField(max_length = 50, default="")
    rut = models.IntegerField(null=False,  unique=True)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField(max_length=50, default="")

class Producto(models.Model):
    nombre = models.CharField(max_length = 50, default = "")
    precio = models.FloatField(null = True)
    stock = models.IntegerField(null = True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    Proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)        

class Venta(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField(null=False)
    descuento = models.FloatField(null = True)
    monto_final = models.FloatField(null = True)
    cantidad = models.IntegerField(null = False)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto, self.cantidad)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default="")
    telefono = models.IntegerField(null = True)
    rut = models.IntegerField(null = False, unique = True) 
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)
