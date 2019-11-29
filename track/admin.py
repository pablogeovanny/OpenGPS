from django.contrib import admin


from .models import Device, Reg
from .models import juan_8356_2019_07_03, juan_8356_2019_07_05, juan_8356_2019_07_06, juan_8356_2019_07_09, juan_9012_2019_07_13, juan_9012_2019_07_16, ana_0684_2019_07_17, ana_0684_2019_07_18, ana_0684_2019_07_19, ventasexpres_1847_2019_07_20, ventasexpres_1847_2019_07_22, ventasexpres_1847_2019_07_23, ventasexpres_9656_2019_07_24, ventasexpres_9656_2019_07_25, superlimpio_6468_2019_07_29, superlimpio_6468_2019_07_30, superlimpio_6468_2019_07_31
from leaflet.admin import LeafletGeoAdmin

class DeviceAdmin(LeafletGeoAdmin):
    list_display = ('IMEI', 'Description', 'User')
class RegAdmin(LeafletGeoAdmin):
    list_display = ('Day', 'Description', 'User')
class juan_8356_2019_07_03Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class juan_8356_2019_07_05Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class juan_8356_2019_07_06Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class juan_8356_2019_07_09Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class juan_9012_2019_07_13Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class juan_9012_2019_07_16Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ana_0684_2019_07_17Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ana_0684_2019_07_18Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ana_0684_2019_07_19Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ventasexpres_1847_2019_07_20Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ventasexpres_1847_2019_07_22Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ventasexpres_1847_2019_07_23Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ventasexpres_9656_2019_07_24Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class ventasexpres_9656_2019_07_25Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class superlimpio_6468_2019_07_29Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class superlimpio_6468_2019_07_30Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')
class superlimpio_6468_2019_07_31Admin(LeafletGeoAdmin):
    list_display = ('Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Distance')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Reg, RegAdmin)
admin.site.register(juan_8356_2019_07_03, juan_8356_2019_07_03Admin)
admin.site.register(juan_8356_2019_07_05, juan_8356_2019_07_05Admin)
admin.site.register(juan_8356_2019_07_06, juan_8356_2019_07_06Admin)
admin.site.register(juan_8356_2019_07_09, juan_8356_2019_07_09Admin)
admin.site.register(juan_9012_2019_07_13, juan_9012_2019_07_13Admin)
admin.site.register(juan_9012_2019_07_16, juan_9012_2019_07_16Admin)
admin.site.register(ana_0684_2019_07_17, ana_0684_2019_07_17Admin)
admin.site.register(ana_0684_2019_07_18, ana_0684_2019_07_18Admin)
admin.site.register(ana_0684_2019_07_19, ana_0684_2019_07_19Admin)
admin.site.register(ventasexpres_1847_2019_07_20, ventasexpres_1847_2019_07_20Admin)
admin.site.register(ventasexpres_1847_2019_07_22, ventasexpres_1847_2019_07_22Admin)
admin.site.register(ventasexpres_1847_2019_07_23, ventasexpres_1847_2019_07_23Admin)
admin.site.register(ventasexpres_9656_2019_07_24, ventasexpres_9656_2019_07_24Admin)
admin.site.register(ventasexpres_9656_2019_07_25, ventasexpres_9656_2019_07_25Admin)
admin.site.register(superlimpio_6468_2019_07_29, superlimpio_6468_2019_07_29Admin)
admin.site.register(superlimpio_6468_2019_07_30, superlimpio_6468_2019_07_30Admin)
admin.site.register(superlimpio_6468_2019_07_31, superlimpio_6468_2019_07_31Admin)