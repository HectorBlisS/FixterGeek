from django.conf.urls import url
from . import views



urlpatterns=[

	url(r'^(?P<slug>[-\w]+)/$',
		views.Wework.as_view(),
		name="detalle"),
	#Ajax Call
	url(r'^descuento/(?P<amount>\d+)/(?P<cupon>[-\w]+)/$',
		views.Descuento.as_view(),
		name="descuento")

	# url(r'^todos/$',
	# 	views.Todos.as_view(),
	# 	name="todos"),

	# url(r'^(?P<slug>[-\w]+)/$',
	# 	views.DetalleEvento.as_view(),
	# 	name="detalle"),

	# url(r'^(?P<evento>[-\w]+)/aplicar$',
	# 	views.Aplicacion.as_view(),
	# 	name="aplicacion"),






]