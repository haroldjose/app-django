from django.db import models
from .validators import validar_monto, validar_apellido, validar_entrada

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=100, validators=[validar_entrada])
    apellido=models.CharField(max_length=100, validators=[validar_apellido])
    correo=models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    moneda=models.DecimalField(max_digits=100, decimal_places=2)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)

class Tipotransaccion(models.Model):
    descripcion=models.TextField(max_length=100)

    def __str__(self):
        return self.descripcion


class Transaccion(models.Model):
    monto=models.DecimalField(max_digits=100, decimal_places=2,validators=[validar_monto])
    cuenta=models.ForeignKey(Cuenta,on_delete=models.CASCADE)
    tipotransaccion=models.ForeignKey(Tipotransaccion,on_delete=models.CASCADE) 



    
        
