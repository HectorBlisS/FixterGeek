from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Evento(models.Model):
	titulo=models.CharField(max_length=50)
	slug=models.SlugField(max_length=60,null=True,blank=True,unique=True)
	descripcion=models.TextField()
	detalles=models.TextField()
	fecha=models.DateTimeField()
	direccion=models.TextField()
	logo=models.ImageField(upload_to='logos',null=True,blank=True)
	portada=models.ImageField(upload_to='eventos',null=True,blank=True)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('eventos:detalle',args=[self.slug])

class Registro(models.Model):
	usuario=models.OneToOneField(settings.AUTH_USER_MODEL)
	amigos=models.IntegerField()
	evento=models.ForeignKey(Evento,related_name='registros')

	def __str__(self):
		return "{} se registro a {}".format(self.usuario,self.evento)

class Aplicant(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="aplicantes")
	motivos = models.TextField()
	evento = models.OneToOneField(Evento)

	def __str__(self):
		return "{} Aplico a {}".format(self.usuario,self.evento)


