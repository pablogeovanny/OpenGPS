#urls to track


from django.conf.urls import url
from django.urls import include, path

from . import views




urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^device/$', views.DeviceListView.as_view(), name='device_list'),

	url(r'^device/taxi/$', views.TaxiListView.as_view(), name='taxi_list'),
	url(r'^device/perro/$', views.PerroListView.as_view(), name='perro_list'),
	url(r'^device/gato/$', views.GatoListView.as_view(), name='gato_list'),
	url(r'^device/vendedor/$', views.VendedorListView.as_view(), name='vendedor_list'),
	url(r'^device/cobrador/$', views.CobradorListView.as_view(), name='cobrador_list'),
	url(r'^device/autodeventas/$', views.AutodeventasListView.as_view(), name='autodeventas_list'),

	url(r'^device/1$', views.juan_8356_2019_07_03DetailView.as_view(), name='test-detail'),
	url(r'^device/2$', views.juan_8356_2019_07_05DetailView.as_view(), name='test-detail'),
	url(r'^device/3$', views.juan_8356_2019_07_06DetailView.as_view(), name='test-detail'),
	url(r'^device/4$', views.juan_8356_2019_07_09DetailView.as_view(), name='test-detail'),
	url(r'^device/5$', views.juan_9012_2019_07_13DetailView.as_view(), name='test-detail'),
	url(r'^device/6$', views.juan_9012_2019_07_16DetailView.as_view(), name='test-detail'),
	url(r'^device/7$', views.ana_0684_2019_07_17DetailView.as_view(), name='test-detail'),
	url(r'^device/8$', views.ana_0684_2019_07_18DetailView.as_view(), name='test-detail'),
	url(r'^device/9$', views.ana_0684_2019_07_19DetailView.as_view(), name='test-detail'),
	url(r'^device/10$', views.ventasexpres_1847_2019_07_20DetailView.as_view(), name='test-detail'),
	url(r'^device/11$', views.ventasexpres_1847_2019_07_22DetailView.as_view(), name='test-detail'),
	url(r'^device/12$', views.ventasexpres_1847_2019_07_23DetailView.as_view(), name='test-detail'),
	url(r'^device/13$', views.ventasexpres_9656_2019_07_24DetailView.as_view(), name='test-detail'),
	url(r'^device/14$', views.ventasexpres_9656_2019_07_25DetailView.as_view(), name='test-detail'),
	url(r'^device/15$', views.superlimpio_6468_2019_07_29DetailView.as_view(), name='test-detail'),
	url(r'^device/16$', views.superlimpio_6468_2019_07_30DetailView.as_view(), name='test-detail'),
	url(r'^device/17$', views.superlimpio_6468_2019_07_31DetailView.as_view(), name='test-detail'),
	url(r'^device/(?P<pk>\d+)$', views.DeviceListView.as_view(), name='test-detail'),
]