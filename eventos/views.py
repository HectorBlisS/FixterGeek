from django.shortcuts import render
from django.views.generic import View
from .models import Evento
from django.shortcuts import get_object_or_404

from .forms import AplicaForm

# Herramienta para restringir acceso
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Todos(View):
	def get(self,request):
		template='eventos/todos.html'
		eventos=Evento.objects.all()
		context={
		'events':eventos,
		}
		return render(request,template,context)

class DetalleEvento(View):
	def get(self,request,slug):
		template = "eventos/detalle.html"
		evento = get_object_or_404(Evento,slug=slug)
		context = {
		'evento':evento,
		}
		return render(request,template,context)

class Aplicacion(View):
	@method_decorator(login_required(login_url='login'))
	def get(self,request,evento):
		evento = get_object_or_404(Evento,slug=evento)
		form = AplicaForm()
		template = 'eventos/aplica.html'
		context = {
		'form':form,
		'evento':evento,
		}
		return render(request,template,context)


	def post(self,request,evento):
		evento = get_object_or_404(Evento,slug=evento)
		form = AplicaForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.evento = evento
			try:
				f.usuario = request.user
				f.save()
			except:
				pass
		template = 'eventos/aplica.html'

		return render(request,template,{'recibido':True,'evento':evento})

















