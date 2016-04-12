from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View



class Home(View):
	def get(self, request):
		return redirect('dashboard')
