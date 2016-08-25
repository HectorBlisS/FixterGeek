from django.contrib import admin
from .models import Apply

class ApplyAdmin(admin.ModelAdmin):
	list_display = ['user','tel','tel2','path']
	list_filter = ['path']


admin.site.register(Apply, ApplyAdmin)