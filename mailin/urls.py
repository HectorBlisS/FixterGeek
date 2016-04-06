from django.conf.urls import url
from . import views


urlpatterns=[

	url(r'^masivo/$',
		views.Masivo.as_view(),
		name="masivo"),

]