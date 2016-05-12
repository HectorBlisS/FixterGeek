from django.shortcuts import render
from django.views.generic import View
from .models import Evento
from django.shortcuts import get_object_or_404



class Todos(View):
	def get(self,request):
		template='eventos/todos.html'
		eventos=Evento.objects.all()
		context={
		'events':eventos,
		}
		return render(request,template,context)

class DetalleEvento(View):
	def get(self,request,slug,id):
		template = "eventos/detalle.html"
		evento = get_object_or_404(Evento,slug=slug,id=id)
		context = {
		'evento':evento,
		}
		return render(request,template,context)



