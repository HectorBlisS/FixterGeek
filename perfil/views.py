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
		form = ProfileForm(instance=request.user)

		context={
		'form':form,
		}
		# saludo.delay('Hola blissi')
		return render(request,template,context)

	def post(self,request):
		if request.POST.get('updateInfo'):
			form = ProfileForm(data = request.POST, instance = request.user)
			print(form)
			if form.is_valid():
				form.save()
				messages.success(request,'Tus datos fueron actualizados')
		else:
			messages.error(request,'Hubo un error, intenta más tarde')
		return redirect('dashboard')





