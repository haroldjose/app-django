from rest_framework import serializers

from .models import Cliente
from .models import Cuenta
from .models import Tipotransaccion
from .models import Transaccion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields= "__all__"


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cuenta
        fields= "__all__"


class TipotransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tipotransaccion
        fields= "__all__"


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaccion
        fields= "__all__"