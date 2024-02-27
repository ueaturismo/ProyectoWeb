from django.contrib import admin
from .models import CategoriaProd,Producto

# Register your models here.

class categoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class productoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(CategoriaProd,categoriaProdAdmin)
admin.site.register(Producto,productoAdmin)