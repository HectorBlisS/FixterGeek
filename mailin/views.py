from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View



class Masivo(View):
	def get(self,request):
		template='mailin/masivo.html'
		context={
		}
		return render(request,template,context)

	def post(self,request):
		try:
			email_masivo()
			print("Exito al enviar mails")
		except Exception as e:
			print ("Error al intentar enviar mails: ",e)

		return redirect('mailin:masivo')



# Funcion para enviar Email
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

def email_masivo():
	subject="Pachuca Django Meetup"
	to=[
	'bremin_11.20@hotmail.com',
	'rotcehcm@hotmail.com',
	'admin@fixter.org',
	'administrador.otech@uaeh.edu.mx',
	'restrell_2@hotmail.com',
	'restrell@yahoo.com.mx',
	'restrell.otech@uaeh.edu.mx',
	'contacto@fixter.org'
	]
	from_email='contacto@fixter.org'
	ctx={}

	# message=get_template("email1.html").render(Context(ctx))
	message=get_template("email1.html").render(ctx)
	msg=EmailMessage(subject,message,to=to,from_email=from_email)
	msg.content_subtype='html'
	msg.send()

def email_gracias(lista):
	subject="Fixter.Geek"
	to=lista
	from_email='contacto@fixter.org'
	ctx={}

	# message=get_template("email1.html").render(Context(ctx))
	message=get_template("email_post_curso.html").render(ctx)
	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
	msg.content_subtype='html'
	msg.send()


class Gracias(View):
	def get(self,request):
		template = 'mailin/gracias.html'
		return render(request,template)
	def post(self,request):
		vlista = request.POST.get('correos')
		print('vlista: ',vlista)
		lista = vlista.split(',')
		print('lista: ',lista)
		try:
			email_gracias(lista)
			return HttpResponse('Ya')
		except:
			return HttpResponse('Error al enviar')

