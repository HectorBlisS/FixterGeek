from django.shortcuts import render
from django.views.generic import View, TemplateView
import conekta
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages



class Terminos(TemplateView):
	template_name = "pagos/condiciones.html"


class Pago(View):
	@method_decorator(login_required)
	def get(self,request, monto=None):
		template_name = "pagos/pago.html"

		if monto:
			context = {'amount':monto}
			return render(request,template_name,context) 
		try:
			tipo = request.user.applys.all()[0].tipo
			if tipo == 'Beca 20%':
				amount = 9600
			elif tipo == 'Beca 50%':
				amount = 6000
			elif tipo == 'Beca 70%':
				amount = 3600
			elif tipo == 'Beca 80%':
				amount = 2400
			context = {'amount':amount}
			print('lo logre')
		except:
			print('except')
			context = {'amount':12000}
		return render(request,template_name,context)

	@method_decorator(login_required)
	def post(self,request, monto=None):
		template_name = "pagos/pago_status.html"
		conekta.api_key = 'key_osrUjhK6DPrmsMs5NRUjwA'
		# amount = int(request.POST.get('amount'))*100
		if not monto:
			amount = int(request.POST.get('amount'))*100
		else:
			amount = int(monto)*100
		tel = request.POST.get('tel')
		print(request.POST.get('conektaTokenId'))
		print('el cargo: ',amount)
		# print('el tel: ',request.user.aplicantes.tel)

		diccionario = {
			  "description":"Fixter.Camp con Beca",
			  "amount": amount,
			  "currency":"MXN",
			  "reference_id":"FixCamp001",
			  "card": request.POST.get('conektaTokenId'),
			  # "monthly_installments": 1,
			  "details": {
			    "name": request.user.first_name+' '+request.user.last_name ,
			    "phone": tel,
			    "email": request.user.email,
			    "line_items": [{
			      "name": "Fixter.Camp",
			      "description": "Curso Presencial y en linea con beca de descuento",
			      "unit_price": amount,
			      "quantity": 1,
			      "sku": "fixcamp001",
			      "category": "course"
			    }],

			  }
			}

		if request.POST.get('meses'):
			diccionario['monthly_installments'] = request.POST.get('meses')


		try:
			print('entre al try ',conekta.api_key)

			charge = conekta.Charge.create(diccionario)

			print (charge.status)			
			context = {'exito':True,'charge':charge}
			messages.success(request, charge.status)
			try:
				request.user.aplicantes.pago = True
				request.user.aplicantes.save()
			except:
				pass
			return render(request,template_name,context)
		except conekta.ConektaError as e:
			print (e)
			messages.error(request, e)
			context = {'exito':False,}
			return render(request,template_name,context)

		# print('estoy antes del render')
		
