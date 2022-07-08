from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop,Merchandise,Factory,Bank,Elevation,Country,\
    Cities

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Factory)
admin.site.register(Elevation)
admin.site.register(Country)
admin.site.register(Bank)
admin.site.register(Cities)
