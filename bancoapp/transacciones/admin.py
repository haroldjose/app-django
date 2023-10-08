from django.contrib import admin

from .models import Cliente
from .models import Cuenta
from .models import Tipotransaccion
from .models import Transaccion
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    search_fields=('nombre')
admin.site.register(Cliente)


class CuentaAdmin(admin.ModelAdmin):
    list_display=('moneda','cliente')
    
admin.site.register(Cuenta,CuentaAdmin)


admin.site.register(Tipotransaccion)


class TransaccionAdmin(admin.ModelAdmin):
    list_display=('monto','cuenta','tipotransaccion')
admin.site.register(Transaccion, TransaccionAdmin)
