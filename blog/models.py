from django.db import models

# Create your models here.
class Animal(models.Model):
	nome = models.CharField(max_length = 100)
	foto = models.URLField()
	def __str__(selfie):
		return selfie.nome
