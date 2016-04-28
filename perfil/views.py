from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .tasks import saludo



class DashBoard(View):
	@method_decorator(login_required)
	def get(self,request):
		template="perfil/dashboard.html"
		context={
		
		}
		saludo('Hola blissi')
		return render(request,template,context)
