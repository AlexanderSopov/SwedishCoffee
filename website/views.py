from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import MenuItem, Projects, Page, Entry, EmailContact
from django.db.models import F
from .forms import EmailForm
# Create your views here.


# Base Context for static parts of the website.
#In other words: parts of the site that don't vary
def baseContext():
	return {"menu": get_list_or_404(MenuItem, ),
		"logoPath":"website/images/coffe_cup.png",
		"form": EmailForm()}



def index(request):
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			mail = form.cleaned_data['your_email']
			model = EmailContact(customer_email= mail)
			model.save()
			#TODO: ping the user to verify everything went OK!
	page = get_object_or_404(Page, title="Swedish Coffee")
	projects = get_list_or_404(Projects)
	context = {
		"page": page,
		"projects": projects
	}
	context.update(baseContext())

	return render(request, "website/index.html", context)


def projects(request):
	projects = get_list_or_404(Projects)
	context = {
		"page": {"title":"Projects"},
		"projects": projects
	}
	context.update(baseContext())
	return render(request, "website/index.html", context)



def about(request):
	aboutPage = get_object_or_404(Page, title="About")
	entry = get_object_or_404(Entry, page=aboutPage.id)
	context = {
		"page": aboutPage,
		"entry": entry
	}
	context.update(baseContext())
	return render(request, "website/about.html", context)


def blog(request):
	blogPage = get_object_or_404(Page, title="Blog")
	entries = get_list_or_404(Entry.objects.order_by(F('pub_date').desc()), page=blogPage.id ) # erase the first hashtag and the closing paranthese to filter for entries who are connected to the blog
	context = {
		"entries": entries
	}
	context.update(baseContext())

	return render(request, "website/blog.html", context)

def blogEntry(request, pk):
	entry = get_object_or_404(Entry, id=pk)
	context={
			"entry":entry
		}
	context.update(baseContext())
	return render(request, "website/blogEntry.html", context)

def projectPage(request, pk):
	page = get_object_or_404(Page, pk=pk)
	entries = get_list_or_404(Entry, page=pk)
	context={
		"entries":entries,
		"page":page
		}
	context.update(baseContext())
	return render(request, "website/projectPage.html", context)

