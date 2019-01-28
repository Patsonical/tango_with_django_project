from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {"bold_message" : "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, "rango/index.html", context=context_dict)

def about(request):
	context_dict = {}
	return render(request, "rango/about.html", context=context_dict)
	#response = "Rango says here is the about page. </br> <a href='/rango/'>Index</a>"
	#return HttpResponse(response)
