from django.db import models
from django.contrib.auth.models import User
from eventos.models import Evento
# from django.conf import settings


class Apply(models.Model):
	BECA_CHOICES = (
		('Beca 20%','Beca 20%'),
		('Beca 50%', 'Beca 50%'),
		('Beca 70%', 'Beca 70%'),
		('Beca 80%', 'Beca 80%'),
		('Beca 99%', 'Beca 99%')
		)
	Choices=(
		(True,'Si la necesito'),
		(False,'No, que la aproveche alguien más'),
		)
	Paths = (
		('servers / Semanal','Backend & Servers / Semanal'),
		('desarrollo_web / Semanal', 'Desarrollo Web / Semanal'),
		('desarrollo_web / Sabatino','Desarrollo Web  / Sabatino'),
		('intro_al_codigo / Semanal','Intro al código / Semanal'),
		('intro_al_codigo / Sabatino','Intro al código / Sabatino')
		)

	motivos = models.TextField()
	beca = models.BooleanField(choices=Choices, default=False)
	tipo = models.CharField(max_length=50, choices=BECA_CHOICES,default='Beca 20%',blank=True,null=True)
	porque = models.TextField(blank=True,null=True)
	tel = models.CharField(max_length=50)
	tel2 = models.CharField(max_length=50,blank=True,null=True)
	path = models.CharField(max_length=140,blank=True,null=True,choices=Paths,default="Backend Path")
	fecha = models.DateTimeField(auto_now=True,blank=True,null=True)
	notas = models.CharField(max_length=500, null=True,blank=True)
	pago = models.NullBooleanField(null=True,blank=True,default=False)
	inscrito = models.NullBooleanField(null=True,blank=True,default=False)
	contactado = models.BooleanField(default=False)
	fecha_de_contacto = models.DateTimeField(null=True,blank=True)
	user = models.ForeignKey(User,related_name='applys')
	evento = models.ForeignKey(Evento,related_name='applys')

	def __str__(self):
		return "{} aplico a {}".format(self.user,self.evento)



