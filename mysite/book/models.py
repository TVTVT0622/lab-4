from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=20)
	authorid = models.IntegerField()
	age = models.IntegerField()
	country = models.CharField(max_length=20)

class Book(models.Model):
	title = models.CharField(max_length=50)
	isbn = models.CharField(max_length=50)
	authorid = models.ForeignKey(Author)
	publisher = models.CharField(max_length=50)
	publication_date = models.CharField(max_length=20)
	price = models.IntegerField()