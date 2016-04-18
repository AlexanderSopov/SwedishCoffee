from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import MenuItem, Projects
# Create your views here.

def index(request):
	menu = get_list_or_404(MenuItem, )
	project = get_list_or_404(Projects)
	project1 = [
			{
				"imgUrl": "website/images/background.png",
				"introduction": "This is greatness, revisited",
				"title": "Stub"
			},
			{
				"imgUrl": "website/images/background.png",
				"introduction": "This is greatness, revisited",
				"title": "Stub"
			},
			{
				"imgUrl": "website/images/background.png",
				"introduction": "This is greatness, revisited",
				"title": "Stub"
			}
		]
	projects= project+project1
	print(projects)
	return render(request, "website/index.html", {
		"page": {"title":"hej"},
		"logoPath":"",
		"menu": menu,
		"projects": projects
	})	
