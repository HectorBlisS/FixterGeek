from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import EncuestaForm
from django.contrib import messages


class newHome(TemplateView):
	template_name="main/home.html"

class Next(TemplateView):
	template_name="main/next.html"

class Tour(TemplateView):
	template_name="main/tour.html"

class Encuesta(View):
	def get(self, request):
		template_name="main/encuesta.html"
		return render(request, template_name)

	def post(self, request):
		form = EncuestaForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Gracias por tus comentarios")
		return redirect('main:home')

		
