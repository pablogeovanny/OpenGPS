from django.shortcuts import render


from .models import Device, Reg
from .models import juan_8356_2019_07_03, juan_8356_2019_07_05, juan_8356_2019_07_06, juan_8356_2019_07_09, juan_9012_2019_07_13, juan_9012_2019_07_16, ana_0684_2019_07_17, ana_0684_2019_07_18, ana_0684_2019_07_19, ventasexpres_1847_2019_07_20, ventasexpres_1847_2019_07_22, ventasexpres_1847_2019_07_23, ventasexpres_9656_2019_07_24, ventasexpres_9656_2019_07_25, superlimpio_6468_2019_07_29, superlimpio_6468_2019_07_30, superlimpio_6468_2019_07_31
from django.views.generic import DetailView, TemplateView, ListView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User

def index(request):
    num_devices=Device.objects.all().count()
    num_juan_8356_2019_07_03=juan_8356_2019_07_03.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_devices':num_devices,'num_juan_8356_2019_07_03':num_juan_8356_2019_07_03},
    )
class DeviceListView(LoginRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Device
class TaxiListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Reg
  permission_required = "track.view_juan_8356_2019_07_03"
  queryset = Reg.objects.filter(Description="1")#Taxi
class PerroListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Reg
  permission_required = "track.view_juan_8356_2019_07_03"
  queryset = Reg.objects.filter(Description="2")#Perro
class GatoListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Reg
  permission_required = "track.view_ana_0684_2019_07_17"
  queryset = Reg.objects.filter(Description="3")#Gato
class VendedorListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Reg
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
  queryset = Reg.objects.filter(Description="4")#Vendedor
class CobradorListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Reg
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
  queryset = Reg.objects.filter(Description="5")#Cobrador
class AutodeventasListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = Reg
  permission_required = "track.view_superlimpio_6468_2019_07_29"
  queryset = Reg.objects.filter(Description="6")#Autodeventas

class juan_8356_2019_07_03DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = juan_8356_2019_07_03
  permission_required = "track.view_juan_8356_2019_07_03"
class juan_8356_2019_07_05DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = juan_8356_2019_07_05
  permission_required = "track.view_juan_8356_2019_07_03"
class juan_8356_2019_07_06DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = juan_8356_2019_07_06
  permission_required = "track.view_juan_8356_2019_07_03"
class juan_8356_2019_07_09DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = juan_8356_2019_07_09
  permission_required = "track.view_juan_8356_2019_07_03"
class juan_9012_2019_07_13DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = juan_9012_2019_07_13
  permission_required = "track.view_juan_8356_2019_07_03"
class juan_9012_2019_07_16DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = juan_9012_2019_07_16
  permission_required = "track.view_juan_8356_2019_07_03"
class ana_0684_2019_07_17DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ana_0684_2019_07_17
  permission_required = "track.view_ana_0684_2019_07_17"
class ana_0684_2019_07_18DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ana_0684_2019_07_18
  permission_required = "track.view_ana_0684_2019_07_17"
class ana_0684_2019_07_19DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ana_0684_2019_07_19
  permission_required = "track.view_ana_0684_2019_07_17"
class ventasexpres_1847_2019_07_20DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ventasexpres_1847_2019_07_20
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
class ventasexpres_1847_2019_07_22DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ventasexpres_1847_2019_07_22
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
class ventasexpres_1847_2019_07_23DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ventasexpres_1847_2019_07_23
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
class ventasexpres_9656_2019_07_24DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ventasexpres_9656_2019_07_24
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
class ventasexpres_9656_2019_07_25DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = ventasexpres_9656_2019_07_25
  permission_required = "track.view_ventasexpres_1847_2019_07_20"
class superlimpio_6468_2019_07_29DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = superlimpio_6468_2019_07_29
  permission_required = "track.view_superlimpio_6468_2019_07_29"
class superlimpio_6468_2019_07_30DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = superlimpio_6468_2019_07_30
  permission_required = "track.view_superlimpio_6468_2019_07_29"
class superlimpio_6468_2019_07_31DetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
  login_url = ''
  redirect_field_name = 'redirect_to'
  model = superlimpio_6468_2019_07_31
  permission_required = "track.view_superlimpio_6468_2019_07_29"