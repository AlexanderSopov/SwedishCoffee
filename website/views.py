from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import MenuItem, Projects, Page, Entry
# Create your views here.



baseContext = {"menu": get_list_or_404(MenuItem, ),
		"logoPath":"website/images/coffe_cup.png"}



def index(request):
	menu = get_list_or_404(MenuItem, )
	projects = get_list_or_404(Projects)
	context = {
		"page": {"title":"Swedish Coffee"},
		"menu": menu,
		"projects": projects
	}
	context.update(baseContext)

	return render(request, "website/index.html", context)


def projects(request):
	menu = get_list_or_404(MenuItem, )
	projects = get_list_or_404(Projects)
	return render(request, "website/index.html", {**{
		"page": {"title":"Projects"},
		"menu": menu,
		"projects": projects
	}, **baseContext} )


def projectPage(request, pk):
	page = get_object_or_404(Page, pk=pk)
	entries = get_list_or_404(Entry, page=pk)
	return render(request, "website/projectPage.html", {**{
		"entries":entries,
		"page":page
		},**baseContext})