from django.core.exceptions import ValidationError

def validar_monto(value):
    if value <= 0: 
        raise ValidationError('el monto no puede ser ingresado monto negativo o 0 ',params={'value':value},)

def validar_apellido(texto):
    if texto.isalpha():
        raise ValidationError('El campo contiene numeros ',params={'value':texto},) 
    

def validar_entrada(dato):
    if len(dato) > 5:
        raise ValidationError('el campo excede cantidad de caracteres ',params={'value':dato},) 