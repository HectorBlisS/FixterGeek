from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostForm, ComentarioForm
from django.contrib import messages


class Home(View):
	def get(self,request):
		template_name = 'posts/home.html'
		form1 = PostForm()
		
		context={
		'form1':form1,

		}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Post Guardado con Exito ^_^')
		else:
			messages.error(request,'Algo Falló, post no guardad X_X')
		return redirect('home')





