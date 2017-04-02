from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import Template, Suscriptor


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

class Beca(View):
	@method_decorator(login_required())
	def get(self,request):
		template_name = "mailin/hackaton.html"
		return render(request,template_name)

	def post(self,request):
		mails = request.POST.get('mails').split(",")
		try:
			enviar_mails(mails,"correos/beca.html","¡Felicidades!")
			messages.success(request,"correos enviados")
		except:
			messages.error(request, "Error al envíar intentalo nuevamente")
		return redirect('mailin:beca')

class Info(View):
		@method_decorator(login_required())
		def get(self, request):
			template_name = "mailin/xmas.html"
			return render(request, template_name)

		def post(self, request):
			mails = request.POST.get('mails').split(",")
			try:
				enviar_mails(mails, "correos/info.html", "Crea tus propias Apps como todo un pro")
				messages.success(request, "correos enviados")
			except:
				messages.error(request, "Error al envíar intentalo nuevamente")
			return redirect('mailin:info')

# # Funcion para enviar Email
# from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

def enviar_mails(mails,template="correos/info.html",subject="Fixter Info"):
	subject=subject
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





class New(View):
	"""
	1.- subir imagenes con tamaño definido
	2.- colocar texto en diferentes secciones segun template
	3.- titulos
	4.- agregar dinamicamente secciones
	5.- cambiar colores y diseño
	6.- try markdown *DONE*
	7.- get emails automaticamente

	Doing: 2
"""
	def get(self, request, pk=None):

		template_name = "mailin/medium.html"
		templates = Template.objects.all()
		context = {
			'templates':templates,
		}

		if pk:
			t = get_object_or_404(Template, id=pk)
			context['section'] = t.nombre
			context['template'] = t

		return render(request, template_name, context)

	def post(self, request):
		# mark = request.POST.get('mark')
		mark = request.POST
		ctx = {
		'mensaje':mark
		}
		
		print(medium_mail(ctx))
		messages.success(request, 'se envió')
		# except:
		# 	messages.error(request, 'no se envió')
		return redirect('mailin:new')


def medium_mail(
	ctx={},
	to=['contacto@fixter.org'],
	from_email="admin@fixter.org",
	subject="test",
	):
	# subject="Fixter.Geek"
	# to=lista
	# from_email='contacto@fixter.org'
	# ctx={}

	# message=get_template("email1.html").render(Context(ctx))
	message=get_template("correos/medium_mail.html").render(ctx)
	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
	msg.content_subtype='html'
	return msg.send()



class Temario(View):
	def get(self, request, token=None):
		if token:
			template_name = 'mailin/adjunto.html'
		else:
			template_name = 'mailin/landing_adjunto.html'
		# return redirect('/static/pdf_files/Temario.pdf')
		return render(request, template_name)

	def post(self, request):
		mail = request.POST.get('mail')
		name = request.POST.get('name')
		tel = request.POST.get('tel')
		try:
			adjunto([mail])
			Suscriptor.objects.create(name=name, tel=tel, email=mail)
			messages.success(request, "El temario fué enviado a tu correo =D verificalo!")
		except:
			messages.error(request, "El correo no pudo enviarse, prueba con otro correo")
		return redirect('mailin:temario')




def adjunto(
	to=['contacto@fixter.org'],
	from_email="admin@fixter.org",
	subject="Temario FixterCamp3",
	ctx={},
	):
	# subject="Fixter.Geek"
	# to=lista
	# from_email='contacto@fixter.org'
	# ctx={}

	# message=get_template("email1.html").render(Context(ctx))
	message=get_template("correos/temario.html").render(ctx)
	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
	msg.content_subtype='html'
	msg.send()



class Mensaje(View):
	def post(self, request):
		datos = {
		'nombre':request.POST.get('nombre'),
		'email':request.POST.get('email'),
		'tel':request.POST.get('tel'),
		'msj':request.POST.get('msj')
		}
		if not request.POST.get('msj'):
			datos['msj'] = 'Quiero recibir mas informacion porfavor'
		# print(datos)
		try:
			mensajeSend(datos)
			messages.success(request, 'Tu mensaje ha sido enviado con éxito pronto nos comunicaremos contigo')
		except:
			messages.error(request, 'Tu mensaje no se puedo enviar, vuelve a intentar')
		return redirect('main:home')




def mensajeSend(datos):
	to=['admin@fixter.org']
	from_email='admin@fixter.org'
	subject="Mensaje nuevo Fixter.camp"
	ctx=datos

	# message=get_template("email1.html").render(Context(ctx))
	message=get_template("mailin/mensaje.html").render(ctx)
	msg=EmailMessage(subject,message,bcc=to,from_email=from_email)
	msg.content_subtype='html'
	return msg.send()

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

