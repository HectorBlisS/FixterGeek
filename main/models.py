from django.db import models

class Encuesta(models.Model):
	path = models.CharField(max_length=140)
	satisfy = models.CharField(max_length=10)
	rank = models.CharField(max_length=10)
	observations = models.TextField()
	repeat = models.CharField(max_length=10)

	def __str__(self):
		return "Encuesta para {}".format(self.path)
