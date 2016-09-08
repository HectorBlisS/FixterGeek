from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^pago/$',
		views.Pago.as_view(),
		name="pago"),
	url(r'^terminos/$',
		views.Terminos.as_view(),
		name="terminos"),
	url(r'^pago/(?P<monto>\d+)/$',
		views.Pago.as_view(),
		name="wework"),
]