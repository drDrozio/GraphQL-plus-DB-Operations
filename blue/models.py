from django.db import models

# Create your models here.
class Blue(models.Model):
	title = models.CharField(("title"),max_length=50)
	content = models.CharField(("content"),max_length=50)
	app_name = models.CharField(("app_name"),max_length=50)

	def __str__(self):
		return self.title


class Language(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Framework(models.Model):
	name = models.CharField(max_length=50)
	langauge = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=25)

	def __str__(self):
		return self.title

class Character(models.Model):
	name = models.CharField(max_length=20)
	movies = models.ManyToManyField(Movie)

	def __str__(self):
		return self.name
