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

