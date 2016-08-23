from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static 
from perfil import urls as PerfilUrls
from eventos import urls as EventosUrls
from mailin import urls as MailinUrls
from main import urls as MainUrls
from pagos import urls as pagosUrls
from applys import urls as applyUrls

from social.apps.django_app import urls as socialUrls




urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^perfil/',
    	include(PerfilUrls)),

    url(r'^eventos/',
    	include(EventosUrls,namespace='eventos')),

    url(r'^mailin/',
        include(MailinUrls,namespace='mailin')),

        # Social Auth
    url('social-auth/',
    	include(socialUrls,
    		namespace="social")),
    # Pagos con conekta
    url(r'^pagos/',
        include(pagosUrls,
            namespace="pagos")),

    url(r'^apply/',
        include(applyUrls)),

    url(r'^',
        include(MainUrls, namespace='main')),

    url(
        regex=r'^media/(?P<path>.*)$',
        view='django.views.static.serve',
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),


]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT)
