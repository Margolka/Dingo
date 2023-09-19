from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting(request):
   return HttpResponse("Hello World!")

def greeting_name(request, name):
   return HttpResponse("Hello " + name.capitalize() +"!")
