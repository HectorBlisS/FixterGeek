from django.conf.urls import url
from . import views


urlpatterns=[

	url(r'^patrocinio/$',
		views.Patrocinio.as_view(),
		name="patrocinio"),

	url(r'^beca/$',
		views.Beca.as_view(),
		name="beca"),

	url(r'^info/$',
		views.Info.as_view(),
		name="info"),

	url(r'^new/(?P<pk>\d+)/$',
		views.New.as_view(),
		name="preview"),

	url(r'^new/$',
		views.New.as_view(),
		name="new"),

	url(r'^temario/(?P<token>[-\w]+)/$',
		views.Temario.as_view(),
		name="temario_token"),

	url(r'^temario/$',
		views.Temario.as_view(),
		name="temario"),

	url(r'^mensaje/$',
		views.Mensaje.as_view(),
		name="mensaje"),

	url(r'^recordatorio/$',
		views.Recordatorio.as_view(),
		name="recordatorio"),

	



	# url(r'^gracias/por/venir/$',
	# 	views.Gracias.as_view(),
		# name="gracias_por_venir"),

]