from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^$',
		views.newHome.as_view(),
		name="home"),
	url(r'^next/',
		views.Next.as_view(),
		name="next"),
	url(r'^tour/',
		views.Tour.as_view(),
		name="tour"),
	
]