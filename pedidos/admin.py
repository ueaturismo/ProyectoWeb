from django.contrib import admin
from .models import Pedido,LineaPedido

# Register your models here.

# class pedidoAdmin(admin.ModelAdmin):
#     readonly_fields=('created','updated')

# class lineapedidoAdmin(admin.ModelAdmin):
#     readonly_fields=('created','updated')

# admin.site.register(Pedido,pedidoAdmin)
admin.site.register([Pedido,LineaPedido])