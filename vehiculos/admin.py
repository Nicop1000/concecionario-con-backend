from django.contrib import admin
from .models import vehiculo, imagenvehiculo, caracteristicas, team

# Register your models here.
class teamAdmin(admin.ModelAdmin):
    model = team

class caracteristicasAdmin(admin.TabularInline):
    model= caracteristicas

class imagenvehiculoAdmin(admin.TabularInline):
    model = imagenvehiculo

class vehiculoAdmin(admin.ModelAdmin):
    inlines = [
        imagenvehiculoAdmin,
        caracteristicasAdmin
    ]    
    
admin.site.register(vehiculo, vehiculoAdmin)
admin.site.register(team, teamAdmin)