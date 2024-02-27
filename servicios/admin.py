from django.contrib import admin
from servicios.models import Servicio

# Register your models here.

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Servicio,servicioAdmin)

# admin.site.register(Articulos)
# admin.site.register(Pedidos)