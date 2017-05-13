from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *

# Create your views here.

def inicial(request):
	animais = Animal.objects.all()
	return render(request,'inicial.html', { 'animais': animais})

def contato(request):
	return HttpResponse('<h1><a href="http://www.google.com">clique para abrir o google</a></h1>')


