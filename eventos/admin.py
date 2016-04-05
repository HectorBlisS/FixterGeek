from django.contrib import admin
from . import models

class EventoAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('titulo',)}

admin.site.register(models.Evento, EventoAdmin)

admin.site.register(models.Registro)
