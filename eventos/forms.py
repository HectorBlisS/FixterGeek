from django import forms
from .models import Aplicant
from django.utils.translation import ugettext_lazy as _


class AplicaForm(forms.ModelForm):

	class Meta:
		model = Aplicant
		fields = ['motivos','tel','beca','tipo','porque']
		labels={
		'motivos':_('Dinos, ¿porqué quieres entrar a Fixter.Camp?'),
		'beca':_('¿Crees que necesitas una Beca?'),
		'porque':_('¿Porque consideras que mereces la beca de descuento?'),
		'tel':_('Proporcionanos un Teléfono donde podamos contactarte')
		}
		widgets = {
            'beca': forms.RadioSelect(attrs={'class':'.beca'})
        }




		# 'email':_('Introduce tu correo electrónico')
		# }
		# widgets = {
		# 	'nombre':forms.TextInput(attrs={'class':'rellenito','placeholder':'Tu nombre mijo','id':'morro'}),
		# }