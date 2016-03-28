from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static 
from perfil import urls as PerfilUrls

from social.apps.django_app import urls as socialUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^perfil/',
    	include(PerfilUrls)),

        # Social Auth
    url('social-auth/',
    	include(socialUrls,
    		namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
