from django.shortcuts import render
from django.views.generic import View
from . import models



class Todos(View):
	def get(self,request):
		template='eventos/todos.html'
		eventos=models.Evento.objects.all()
		context={
			'events':eventos
		}
		return render(request,template,context)

