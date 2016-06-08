from django.db import models



class Post(models.Model):
	titulo = models.CharField(max_length=140,blank=True,null=True)
	cuerpo = models.TextField(null=True,blank=True)



class Comentario(models.Model):
	post = models.ForeignKey(Post, related_name='comentarios')
	cuerpo = models.TextField(null=True,blank=True)
