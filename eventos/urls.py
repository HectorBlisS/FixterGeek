from django.conf.urls import url
from . import views



urlpatterns=[

	url(r'^todos/$',
		views.Todos.as_view(),
		name="todos"),

	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
		views.DetalleEvento.as_view(),
		name="detalle"),



]