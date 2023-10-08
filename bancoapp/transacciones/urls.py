from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"clientes", views.ClienteViewSet)
router.register(r"cuentas", views.CuentaViewSet)
router.register(r"tipostransaccion", views.TipotransaccionViewSet)
router.register(r"transacciones", views.TransaccionViewSet)

urlpatterns =[
    path("", views.index, name="index"),
    path('clientes/cantidad/', views.cliente_count, name='clientes_cantidad'),
    path('cuenta/monto/', views.cuenta_count, name='cuenta_monto'),
    path('', include(router.urls)),
]