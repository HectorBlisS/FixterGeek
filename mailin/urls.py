from django.conf.urls import url
from . import views


urlpatterns=[

	url(r'^patrocinio/$',
		views.Patrocinio.as_view(),
		name="patrocinio"),

	# url(r'^gracias/por/venir/$',
	# 	views.Gracias.as_view(),
		# name="gracias_por_venir"),

]