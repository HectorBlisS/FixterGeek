from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.views.generic import View
from .models import Evento, Cupon
from django.shortcuts import get_object_or_404
import json



class Wework(View):
	def get(self, request, slug):
		evento = get_object_or_404(Evento, slug=slug)
		template_name="eventos/detalle.html"
		context = {
		'evento':evento
		}
		return render(request, template_name, context)

class Descuento(View):
	"""
	Vista para Ajax
	"""
	def get(self, request,cupon=None,amount=None):
		amount = int(amount)
		if cupon and amount:
			cupon = get_object_or_404(Cupon,nombre=cupon)
			if cupon.cantidad:
				precio_final = amount - cupon.cantidad
			else:
				precio_final = amount - (amount * cupon.porcentaje)
			return HttpResponse(precio_final)
		else:
			return HttpResponseNotFound('El cupon no es valido')
			
		







# from .forms import AplicaForm

# # Herramienta para restringir acceso
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator



# class Todos(View):
# 	def get(self,request):
# 		template='eventos/todos.html'
# 		eventos=Evento.objects.all()
# 		context={
# 		'events':eventos,
# 		}
# 		return render(request,template,context)

# class DetalleEvento(View):
# 	def get(self,request,slug):
# 		template = "eventos/detalle.html"
# 		evento = get_object_or_404(Evento,slug=slug)
# 		context = {
# 		'evento':evento,
# 		}
# 		return render(request,template,context)

# class Aplicacion(View):
# 	@method_decorator(login_required(login_url='login'))
# 	def get(self,request,evento):
# 		evento = get_object_or_404(Evento,slug=evento)
# 		form = AplicaForm()
# 		template = 'eventos/aplica.html'
# 		context = {
# 		'form':form,
# 		'evento':evento,
# 		}
# 		return render(request,template,context)


# 	def post(self,request,evento):
# 		evento = get_object_or_404(Evento,slug=evento)
# 		form = AplicaForm(request.POST)
# 		if form.is_valid():
# 			f = form.save(commit=False)
# 			f.evento = evento
# 			try:
# 				f.usuario = request.user
# 				f.save()
# 			except:
# 				pass
# 		template = 'eventos/aplica.html'

# 		return render(request,template,{'recibido':True,'evento':evento})

















