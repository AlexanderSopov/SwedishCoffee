from django.db import models
#from tinymce import models as tinymce_models

# Create your models here.


class Page(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	def __str__(self):
		return self.title

class MenuItem(models.Model):
	page = models.ForeignKey(Page)
	def __str__(self):
		return self.page.__str__()

class Projects(models.Model):
	imgUrl = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	introduction = models.TextField()
	page = models.ForeignKey(Page)
	def __str__(self):
		return self.title

	def get_url(self):
		return "projects/", page.url


class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	bio = models.CharField(max_length=420, null=True)
	imgUrl = models.TextField()
	def __str__(self):
		return self.name

class Entry(models.Model):
	page = models.ForeignKey(Page)
	headline = models.CharField(max_length=100)
	body_text = models.TextField() #tinymce_models.HTMLField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	author = models.ForeignKey(Author, null=True)
	nr_of_comments = models.IntegerField()
	imgUrl = models.TextField()
	def __str__(self):
		return self.headline

class EmailContact(models.Model):
	customer_email = models.EmailField(max_length=254)
	def __str__(self):
		return self.customer_email


