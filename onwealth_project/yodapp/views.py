from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Yoda says hey there world! <br/> <a href='/yodapp/about'>About</a>")

def about(request):
	return HttpResponse("Yoda says here is the about page")