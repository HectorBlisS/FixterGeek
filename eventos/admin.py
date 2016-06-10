from django.contrib import admin
from . import models





from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin


class EventoAdmin(ImportExportMixin, admin.ModelAdmin):
	prepopulated_fields={'slug':('titulo',)}

admin.site.register(models.Evento, EventoAdmin)

admin.site.register(models.Registro)

class AplicantAdmin(admin.ModelAdmin):
	list_display = ('usuario','beca','tipo','path','tel','fecha')
	list_filter = ('beca','tipo')
	search_fields =('tel',)
admin.site.register(models.Aplicant, AplicantAdmin)
