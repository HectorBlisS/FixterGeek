from django.shortcuts import render
from django.views.generic import View, TemplateView
import conekta
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Terminos(TemplateView):
	template_name = "pagos/condiciones.html"


class Pago(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = "pagos/pago.html"
		if request.user.aplicantes.tipo:
			if request.user.aplicantes.tipo == 'Beca 20%':
				amount = 9600
			elif request.user.aplicantes.tipo == 'Beca 50%':
				amount = 6000
			elif request.user.aplicantes.tipo == 'Beca 70%':
				amount = 3600
			elif request.user.aplicantes.tipo == 'Beca 80%':
				amount = 2400
			context = {'amount':amount}
		else:
			context = {'amount':12000}
		return render(request,template_name,context)

	@method_decorator(login_required)
	def post(self,request):
		template_name = "pagos/pago_status.html"
		conekta.api_key = 'key_sqCLgHarDSoaR2PWKsTZoA'
		amount = int(request.POST.get('amount'))*100
		print(request.POST.get('conektaTokenId'))
		print('el cargo: ',amount)
		print('el tel: ',request.user.aplicantes.tel)

		diccionario = {
			  "description":"Fixter.Camp con Beca",
			  "amount": amount,
			  "currency":"MXN",
			  "reference_id":"FixCamp001",
			  "card": request.POST.get('conektaTokenId'),
			  # "monthly_installments": 1,
			  "details": {
			    "name": request.user.first_name+' '+request.user.last_name ,
			    "phone": request.user.aplicantes.tel,
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
			request.user.aplicantes.pago = True
			request.user.aplicantes.save()
			return render(request,template_name,context)
		except conekta.ConektaError as e:
			print (e)
			context = {'exito':False,}
			return render(request,template_name,context)

		# print('estoy antes del render')
		
