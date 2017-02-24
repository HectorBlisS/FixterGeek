from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View
from eventos.models import Evento
from .forms import ApplyForm
from .models import Apply
from django.contrib import messages

# Herramienta para restringir acceso
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Inscription

class DoApply(View):
	@method_decorator(login_required(login_url='login'))
	def get(self,request,pk):
		evento = get_object_or_404(Evento,pk=pk)
		try:
			# Apply.objects.get(user=request.user,evento=evento)
			Inscription.objects.get(user=request.user)
			return render(request,'applys/ya_aplico.html')
		except:
			pass
		template_name="applys/do.html"
		form = ApplyForm()
		context = {
		'form':form,
		'evento':evento
		}

		return render(request,template_name,context)

	def post(self,request,pk):
		#Checkamos si el usuario ya aplico
		# evento = get_object_or_404(Evento,pk=pk)
		# form = ApplyForm(request.POST)
		# if form.is_valid():
		# 	app = form.save(commit=False)
		# 	app.user = request.user
		# 	app.evento = evento
		# 	app.save()
		# else:
		# 	template_name="applys/do.html"
		# # evento = get_object_or_404(Evento,pk=pk)
		# 	form = ApplyForm(request.POST)
		# 	context = {
		# 	'form':form
		# 	}
		# 	return render(request,template_name,context)

		#checamos si el usuario ya aplico
		inscripcion = Inscription.objects.filter(user=request.user)
		if not inscripcion:
			try:
				Inscription.objects.create(
						user=request.user,
						nombre=request.POST.get('nombre'),
						email=request.POST.get('email'),
						tel=request.POST.get('tel'),
						path=request.POST.get('path'),
						beca=request.POST.get('beca'),
						why=request.POST.get('why')
					)
				messages.success(request, 'Te has inscrito correctamente, gracias!')
			except:
				messages.error(request, 'Tu inscripción no puedo completarce, intentalo de nuevo.')
				template_name = 'applys/do.html'
				return render(request,template_name)
		else:
			return render(request,'applys/ya_aplico.html')


		template_name = 'applys/gracias.html'
		return render(request,template_name)

