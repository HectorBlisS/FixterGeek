from celery import task
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def saludo(saludo):
	subject='Probando Celery on aws'
	message=saludo
	mail_sent=send_mail(subject,message,'rotcehcm@hotmail.com',['contacto@fixter.org'])
	return mail_sent