from django.conf.urls import url
from . import views


urlpatterns=[

	url(r'^patrocinio/$',
		views.Patrocinio.as_view(),
		name="patrocinio"),

	url(r'^hackaton/$',
		views.Hackaton.as_view(),
		name="hackaton"),

	url(r'^fc3/$',
		views.Fc3.as_view(),
		name="fc3"),

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

	



	# url(r'^gracias/por/venir/$',
	# 	views.Gracias.as_view(),
		# name="gracias_por_venir"),

]