from django.db import models

# Create your models here.
class Blue(models.Model):
	title = models.CharField(("title"),max_length=50)
	content = models.CharField(("content"),max_length=50)
	app_name = models.CharField(("app_name"),max_length=50)

	def __str__(self):
		return self.title