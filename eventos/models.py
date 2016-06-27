from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Evento(models.Model):
	titulo=models.CharField(max_length=50)
	slug=models.SlugField(max_length=60)
	descripcion=models.TextField()
	detalles=models.CharField(max_length=140)
	# precio = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	precio = models.CharField(max_length=10)
	fecha=models.DateTimeField()
	direccion=models.TextField()
	logo=models.ImageField(upload_to='logos',null=True,blank=True)
	portada=models.ImageField(upload_to='eventos',null=True,blank=True)
	boton=models.CharField(max_length=50,null=True,blank=True)

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
	BECA_CHOICES = (
		('Beca 20%','Beca 20%'),
		('Beca 50%', 'Beca 50%'),
		)
	Choices=(
		(True,'Si la necesito'),
		(False,'No, que la aproveche alguien más'),
		)
	Paths = (
		('backend path','Backend Path'),
		('frontend path','Frontend Path'),
		)
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="aplicantes")
	motivos = models.TextField(blank=True,null=True)
	evento = models.ForeignKey(Evento)
	beca = models.BooleanField(choices=Choices, default=False)
	tipo = models.CharField(max_length=50, choices=BECA_CHOICES,default='Beca 20%',blank=True,null=True)
	porque = models.TextField(blank=True,null=True)
	tel = models.CharField(max_length=10,blank=True,null=True)
	path = models.CharField(max_length=140,blank=True,null=True,choices=Paths,default="Frontend Path")
	fecha = models.DateTimeField(auto_now=True,blank=True,null=True)
	notas = models.TextField(null=True,blank=True)
	pago = models.BooleanField(null=True,blank=True,default=False)
	inscrito = models.BooleanField(null=True,blank=True,default=False)
	contactado = models.BooleanField(null=True,blank=True,default=False)


	def __str__(self):
		return "{} Aplico a {}".format(self.usuario,self.evento)

class Mes(models.Model):
	Opciones = (
			('enero','Enero'),
			('febrero','Febrero'),

		)
	nombre = models.CharField(max_length=140,blank=True,null=True,choices=Opciones)

class Dia(models.Model):
	num = models.CharField(max_length=140,blank=True,null=True)
	mes = models.ForeignKey(Mes)









