from django.contrib import admin
from . import models





from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin


class EventoAdmin(ImportExportMixin, admin.ModelAdmin):
	prepopulated_fields={'slug':('titulo',)}

admin.site.register(models.Evento, EventoAdmin)

admin.site.register(models.Registro)

class AplicantAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ('usuario','beca','tipo','path','tel','notas','fecha','contactado','inscrito')
	list_filter = ('beca','tipo','contactado','inscrito')
	search_fields =('tel',)
	list_editable = ['notas','contactado','tipo']
admin.site.register(models.Aplicant, AplicantAdmin)
