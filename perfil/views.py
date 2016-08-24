from django.shortcuts import render,redirect
from django.views.generic import View

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .tasks import saludo

from .forms import ProfileForm


class DashBoard(View):
	@method_decorator(login_required)
	def get(self,request):
		template="perfil/dashboard.html"
		perfil = request.user.userprofile
		form = ProfileForm(instance=perfil)

		context={
		'form':form,
		}
		# saludo.delay('Hola blissi')
		return render(request,template,context)

	def post(self,request):
		perfil = request.user.userprofile
		form = ProfileForm(data = request.POST, instance = perfil)
		if form.is_valid():	
			form.save()
			messages.success(request,'Tus datos fueron actualizados')
		else:
			messages.error(request,'Hubo un error, intenta de nuevo')
		
		template="perfil/dashboard.html"
		form = ProfileForm(instance=perfil)

		context={
		'form':form,
		}
		# saludo.delay('Hola blissi')
		return render(request,template,context)





