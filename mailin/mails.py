from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage





def welcome_mail(datos,para):
	subject="¡Ya eres Parte del Futuro!"
	to=[para]
	from_email='contacto@fixter.org'
	ctx=datos

	message=get_template("welcome.html").render(ctx)
	msg=EmailMessage(subject,message,to=to,from_email=from_email)
	msg.content_subtype='html'
	msg.send()