from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Evento(models.Model):
	titulo=models.CharField(max_length=60)
	slug=models.SlugField(max_length=60)
	descripcion=models.TextField()
	detalles=models.CharField(max_length=140)
	# precio = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	precio = models.IntegerField()
	precio_promo=models.IntegerField()
	fecha=models.DateTimeField()
	direccion=models.TextField()
	logo=models.ImageField(upload_to='logos',null=True,blank=True)
	portada=models.ImageField(upload_to='eventos',null=True,blank=True)
	boton=models.CharField(max_length=50,null=True,blank=True)
	video=models.CharField(max_length=500, null=True,blank=True)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('eventos:detalle',args=[self.slug])










