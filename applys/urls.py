from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^(?P<pk>\d+)/$',views.DoApply.as_view(),name="apply"),
]