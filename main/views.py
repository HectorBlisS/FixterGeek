from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View




class newHome(TemplateView):
	template_name="main/home.html"

class Next(TemplateView):
	template_name="main/next.html"

class Tour(TemplateView):
	template_name="main/tour.html"
