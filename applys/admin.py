from django.contrib import admin
from .models import Apply, Inscription

class ApplyAdmin(admin.ModelAdmin):
	list_display = ['user','tel','tel2','path']
	list_filter = ['path','evento']

class InscriptionAdmin(admin.ModelAdmin):
	list_display = ['id','fecha','nombre','email','tel','path','beca']
	list_filter = ['fecha','path']


admin.site.register(Apply, ApplyAdmin)

admin.site.register(Inscription, InscriptionAdmin)