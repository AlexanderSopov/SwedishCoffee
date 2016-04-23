from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import MenuItem, Projects
# Create your views here.



baseContext = {"menu": get_list_or_404(MenuItem, )}



def index(request):

	print("got to index in website")
	menu = get_list_or_404(MenuItem, )
	projects = get_list_or_404(Projects)
	context = {
		"page": {"title":"hej"},
		"logoPath":"website/images/coffe_cup.png",
		"menu": menu,
		"projects": projects
	}
	context.update(baseContext)

	return render(request, "website/index.html", context)	



def projects(request):
	menu = get_list_or_404(MenuItem, )
	projects = get_list_or_404(Projects)
	return render(request, "website/index.html", {**{
		"page": {"title":"hej"},
		"logoPath":"website/images/coffe_cup.png",
		"menu": menu,
		"projects": projects
	}, **baseContext} )	
