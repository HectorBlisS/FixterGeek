from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^todos/$',
		views.Todos.as_view(),
		name="todos"),

	# url(r'^detalles/(?P<id>\d+)/$',
	# 	views.Todos.as_view(),
	# 	name="todos"),
]