from django import forms
from .models import Apply


class ApplyForm(forms.ModelForm):
	class Meta:
		model = Apply
		fields = ['motivos','tel','tel2','path','beca','porque']
		labels={
			'motivos': 'Cuentanos porque quieres ser parte del FixterCamp',
			'tel':'Tu teléfono personal',
			'tel2':'Algun otro teléfono donde te localizemos',
			'porque':'¿Porqué consideras que eres merecedor de una beca?'
		}