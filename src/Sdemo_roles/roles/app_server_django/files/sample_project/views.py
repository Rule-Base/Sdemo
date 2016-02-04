from django.shortcuts import render
from django.http import HttpResponse

def django_hello_world(self):
   return HttpResponse("Hi there, I'm served from %s!")
