from django.conf.urls import url

from . import views
from django.contrib.auth import views as authviews

urlpatterns=[


	#login / logout urls
	
	url(r'^logout/$',
		authviews.logout,
		name='logout'),

	url(r'^login/$',
		authviews.login,
		name="login"),
	
	url(r'^logout-then-login/$',
		authviews.logout_then_login,
		name='logout_then_login'),
	
	url(r'^$',
		views.DashBoard.as_view(),
		name="dashboard"),

	#Change password urls
	url(r'^password-change/$',
		authviews.password_change,
		name='password_change'),
	url(r'^password-change/done/$',
		authviews.password_change_done,
		name="password_change_done"),
	
	#Restore password urls
	url(r'^password-reset/$',
		authviews.password_reset,
		name="password_reset"),
	url(r'^password-reset/done/$',
		authviews.password_reset_done,
		name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
		authviews.password_reset_confirm,
		name="password_reset_confirm"),
	url(r'^password-reset/complete/$',
		authviews.password_reset_complete,
		name='password_reset_complete'),

	#Url para registro de nuevo usuario
	# url(r'^register/$',
	# 	views.Registro.as_view(),
	# 	name="register"),

	# Editar el perfil
	# url(r'^edit/$',
	# 	views.Editar.as_view(),
	# 	name="edit"),

	

]