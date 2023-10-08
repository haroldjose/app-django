from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

from .models import Cuenta
from .serializers import CuentaSerializer

from .models import Tipotransaccion
from .serializers import TipotransaccionSerializer

from .models import Transaccion
from .serializers import TransaccionSerializer
# Create your views here.

def index(request):
    return HttpResponse("hola mundo")


class ClienteViewSet(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer

class CuentaViewSet(viewsets.ModelViewSet):
    queryset=Cuenta.objects.all()
    serializer_class=CuentaSerializer    

class TipotransaccionViewSet(viewsets.ModelViewSet):
    queryset=Tipotransaccion.objects.all()
    serializer_class=TipotransaccionSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset=Transaccion.objects.all()
    serializer_class=TransaccionSerializer


@api_view(["GET"])
def cliente_count(request):
    """
    Cantida de items registrados en cliente
    """
    try:
        cantidad=Cliente.objects.count()
        return JsonResponse(
            {"cantidad": cantidad },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message":str(e)},safe=False, status=400)


@api_view(["GET"])
def cuenta_count(request):
    """
    auqellos que tienen un monto de 200
    """
    try:
        cantidad=Cuenta.objects.filter(moneda=200).count()
        return JsonResponse(
            {"cantidad": cantidad },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message":str(e)},safe=False, status=400)