# from django.core.files.base import ContentFile
from requests import request, ConnectionError
from .models import UserProfile
from mailin import mails



def save_profile_picture(backend, user, response, is_new,  *args, **kwargs):
	if backend.name == 'facebook' and is_new:
		user_model=user
		user_profile=UserProfile()
		user_profile.user=user_model
		# url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
		ide=response['id']
		correo=response['email']
		print(ide)


		try:
			user_profile.ide=ide
			user_profile.save()

		except ConnectionError:
			pass
			print("Error de conexión")
	# Dando bienvenida
		try:
			datos={
			'usuario':user
			}

			mails.welcome_mail(datos,correo)
			print("enviando correo a: ",correo)
		except:
			print("No se envió el correo")