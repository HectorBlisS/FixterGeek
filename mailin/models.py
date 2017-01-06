from django.db import models



class Template(models.Model):
	nombre = models.CharField(max_length=140)
	espacios = models.IntegerField()
	template = models.CharField(max_length=140)
	img_espacios = models.IntegerField()

	def __str__(self):
		return self.nombre

class Imagen(models.Model):
	img = models.ImageField(upload_to="mailin/images")
	colocacion = models.IntegerField(unique=True)
	template = models.ForeignKey(Template, related_name='imagenes')


class Suscriptor(models.Model):
	name = models.CharField(max_length=200)
	tel = models.CharField(max_length=140)
	email = models.CharField(max_length=140)

	def __str__(self):
		return self.name
	