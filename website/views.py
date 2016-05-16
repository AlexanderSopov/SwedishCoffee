from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import MenuItem, Projects, Page, Entry
# Create your views here.



# Base Context for static parts of the website.
#In other words: parts of the site that don't vary
baseContext = {"menu": get_list_or_404(MenuItem, ),
		"logoPath":"website/images/coffe_cup.png"}



def index(request):
	page = get_object_or_404(Page, title="Swedish Coffee")
	projects = get_list_or_404(Projects)
	context = {
		"page": page,
		"projects": projects
	}
	context.update(baseContext)

	return render(request, "website/index.html", context)


def projects(request):
	projects = get_list_or_404(Projects)
	return render(request, "website/index.html", {**{
		"page": {"title":"Projects"},
		"projects": projects
	}, **baseContext} )



def about(request):
	aboutPage = get_object_or_404(Page, title="About")
	entry = get_object_or_404(Entry, page=aboutPage.id)
	return render(request, "website/about.html", {**{
		"page": aboutPage,
		"entry": entry
	}, **baseContext} )


def blog(request):
	blogPage = get_object_or_404(Page, title="Blog")
	entries = get_list_or_404(Entry, page=blogPage.id)
	return render(request, "website/blog.html", {**{
		"entries": entries
	}, **baseContext} )

def blogEntry(request, pk):
	entry = get_object_or_404(Page, id=pk)
	return render(request, "website/blogEntry.html", {**{
			"entry":entry
		}, **baseContext})

def projectPage(request, pk):
	page = get_object_or_404(Page, pk=pk)
	entries = get_list_or_404(Entry, page=pk)
	return render(request, "website/projectPage.html", {**{
		"entries":entries,
		"page":page
		},**baseContext})