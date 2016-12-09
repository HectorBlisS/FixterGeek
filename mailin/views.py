from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


class Patrocinio(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "mailin/patrocinio.html"
		return render(request,template_name)

	def post(self, request):
		mails = request.POST.get('mails').split(",")
		try:
			enviar_mails(mails)
			messages.success(request,"correos enviados")
		except:
			messages.error(request, "Error al enviar, intentalo nuevamente")
		return redirect('mailin:patrocinio')

class Hackaton(View):
	@method_decorator(login_required())
	def get(self,request):
		template_name = "mailin/hackaton.html"
		return render(request,template_name)

	def post(self,request):
		mails = request.POST.get('mails').split(",")
		try:
			enviar_mails(mails,"hackaton.html")
			messages.success(request,"correos enviados")
		except:
			messages.error(request, "Error al envíar intentalo nuevamente")
		return redirect('mailin:hackaton')

# # Funcion para enviar Email
# from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

def enviar_mails(mails,template="patrocinioMail.html"):
	subject="Mesa de patrocinadores Hackaton 2016"
	to=mails
	from_email='admin@fixter.org'
	# ctx=mails

	# message=get_template("patrocinioMail.html").render(Context(ctx))
	message=get_template(template).render()
	# message=get_template("email1.html").render(ctx)
	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
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







# from django.shortcuts import render, redirect, HttpResponse
# from django.views.generic import View
# from eventos.models import Aplicant
# from django.contrib.auth.models import User

# from django.contrib import messages


# class Masivo(View):
# 	def get(self,request):
# 		template='mailin/masivo.html'
# 		context={
# 		}
# 		return render(request,template,context)

# 	def post(self,request):
# 		to=[]
# 		print(request.POST.get('path'))
# 		if request.POST.get('path')!='all':
# 			alumnos = User.objects.filter(aplicantes__path=request.POST.get('path'))
# 		else:
# 			alumnos = User.objects.filter(aplicantes__inscrito=True)
# 		try:
# 			for i in alumnos:
# 				to.append(i.email)
# 			print(to)
# 		except Exception as e:
# 			messages.error(request,'los correos son icorrectos',e)
# 		context = {
# 		'prueba':'prueba morro',
# 		'titulo':request.POST.get('titulo'),
# 		'to':to,
# 		'parrafo1':request.POST.get('parrafo1'),
# 		'parrafo2':request.POST.get('parrafo2'),
# 		'parrafo3':request.POST.get('parrafo3'),
# 		'imagen':request.POST.get('imagen')

# 		}
# 		try:
# 			email_masivo(context)
# 			print("Exito al enviar mails")
# 			messages.success(request,'Correos enviados')
# 		except Exception as e:
# 			print ("Error al intentar enviar mails: ",e)
# 			messages.error(request,'Error')
# 		return redirect('mailin:masivo')



# # Funcion para enviar Email
# from django.template import Context
# from django.template.loader import get_template
# from django.core.mail import EmailMessage

# def email_masivo(data):
# 	subject=data['titulo']
# 	to=data['to']
# 	from_email='contacto@fixter.org'
# 	ctx=data

# 	message=get_template("email1.html").render(Context(ctx))
# 	# message=get_template("email1.html").render(ctx)
# 	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
# 	msg.content_subtype='html'
# 	msg.send()

# def email_gracias(lista):
# 	subject="Fixter.Geek"
# 	to=lista
# 	from_email='contacto@fixter.org'
# 	ctx={}

# 	# message=get_template("email1.html").render(Context(ctx))
# 	message=get_template("email_post_curso.html").render(ctx)
# 	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
# 	msg.content_subtype='html'
# 	msg.send()


# class Gracias(View):
# 	def get(self,request):
# 		template = 'mailin/gracias.html'
# 		return render(request,template)
# 	def post(self,request):
# 		vlista = request.POST.get('correos')
# 		print('vlista: ',vlista)
# 		lista = vlista.split(',')
# 		print('lista: ',lista)
# 		try:
# 			email_gracias(lista)
# 			return HttpResponse('Ya')
# 		except:
# 			return HttpResponse('Error al enviar')

