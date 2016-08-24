from django.db import models
from django.conf import settings


class UserProfile(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	photo=models.URLField(blank=True,null=True)
	ide=models.CharField(max_length=50,null=True,blank=True)
	correo = models.EmailField(blank=True,null=True)

	def __str__(self):
		return "Perfil de {}".format(self.user)

class Correo(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='correos')
	correo=models.EmailField()
	nombre=models.CharField(max_length=50)

	def __str__(self):
		return "Correo de {}".format(self.user)

