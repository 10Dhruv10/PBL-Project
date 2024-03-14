from django.db import models

class displa(models.Model):
	name = models.CharField("Displa Name", max_length=120)
	year = models.CharField(max_length=60)
	contact = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	material = models.CharField(max_length=60)
	price = models.CharField(max_length=60)

	def __str__(self):
		return self.name