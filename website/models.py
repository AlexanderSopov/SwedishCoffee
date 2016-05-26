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
	def __str__(self):
		return self.name

class Entry(models.Model):
	page = models.ForeignKey(Page)
	headline = models.CharField(max_length=100)
	body_text = models.TextField() #tinymce_models.HTMLField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	authors = models.ManyToManyField(Author)
	nr_of_comments = models.IntegerField()
	imgUrl = models.TextField()
	def __str__(self):
		return self.headline

class emailContact(models.Model):
	customerEmail = models.EmailField(max_length=254)

'''
class Page(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	def __str__(self):
		return self.title


defaultPage = Page(title="Default", url="whatever")



class ProjectPage(Page):
	headline = models.CharField(max_length=100)
	body_text = models.TextField()


class Projects(models.Model):
	imgUrl = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	introduction = models.TextField()
	#page = models.OneToOneField(ProjectPage)
	page = models.ForeignKey(Page, default=defaultPage)
	def __str__(self):
		return self.title


class MenuItem(models.Model):
	page = models.ForeignKey(Page)
	def __str__(self):
		return self.page.__str__()

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	def __str__(self):
		return self.name

class Entry(models.Model):
	page = models.ForeignKey(Page)
	headline = models.CharField(max_length=100)
	body_text = models.TextField() #tinymce_models.HTMLField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	authors = models.ManyToManyField(Author)
	nr_of_comments = models.IntegerField()
	imgUrl = models.TextField()
	def __str__(self):
		return self.headline


'''


