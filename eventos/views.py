from django.shortcuts import render
from django.views.generic import View
from . import models
from django.shortcuts import get_object_or_404



class Todos(View):
	def get(self,request):
		template='eventos/todos.html'
		eventos=models.Evento.objects.all()
		context={
			'events':eventos
		}
		return render(request,template,context)
class DetalleEvento(View):
	def get(self,request,slug):
		template = "eventos/detalle.html"
		evento = get_object_or_404(models.Evento,slug=slug)
		context = {
		'evento':evento,
		}
		return render(request,template,context)

