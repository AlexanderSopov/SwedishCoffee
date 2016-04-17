from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import MenuItem, Projects
# Create your views here.

def index(request):
	menu = get_list_or_404(MenuItem, )
	project = get_object_or_404(Projects, id=1)
	print(project.imgUrl)
	return render(request, "website/index.html", {
		"page": {"title":"hej"},
		"logoPath":"",
		"menu": menu,
		"projects":[
			project,
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

	})	
