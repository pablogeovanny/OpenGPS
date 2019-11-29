


from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import User
from django.urls import reverse

class Device(models.Model):
    IMEI = models.CharField(max_length=100, blank=False)
    Description = models.CharField(max_length=100, blank=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Description
    #def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        #return reverse('Device-detail', args=[str(self.id)])
    class Meta:
        # order of drop-down list items
        ordering = ('id',)
        # plural form in admin view
        verbose_name_plural = 'Devices'
        pass
class Reg(models.Model):
    Day = models.CharField(max_length=100, blank=False)
    Description = models.ForeignKey(Device, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('test-detail', args=[str(self.id)])
class juan_8356_2019_07_03(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class juan_8356_2019_07_05(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class juan_8356_2019_07_06(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class juan_8356_2019_07_09(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class juan_9012_2019_07_13(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class juan_9012_2019_07_16(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ana_0684_2019_07_17(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ana_0684_2019_07_18(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ana_0684_2019_07_19(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ventasexpres_1847_2019_07_20(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ventasexpres_1847_2019_07_22(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ventasexpres_1847_2019_07_23(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ventasexpres_9656_2019_07_24(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class ventasexpres_9656_2019_07_25(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class superlimpio_6468_2019_07_29(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class superlimpio_6468_2019_07_30(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)
class superlimpio_6468_2019_07_31(models.Model):
    Timestamp = models.CharField(max_length=100, blank=False)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Altitude = models.DecimalField(max_digits=4, decimal_places=0)
    Distance = models.DecimalField(max_digits=5, decimal_places=2)