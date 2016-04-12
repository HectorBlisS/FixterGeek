from django.db import models
from django.conf import settings


class UserProfile(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL)
	photo=models.URLField()

class Correo(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='correos')
	correo=models.EmailField()
	nombre=models.CharField(max_length=50)

