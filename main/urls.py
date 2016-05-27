from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^$',
		views.newHome.as_view(),
		name="home"),
]