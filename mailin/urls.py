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

	# url(r'^gracias/por/venir/$',
	# 	views.Gracias.as_view(),
		# name="gracias_por_venir"),

]