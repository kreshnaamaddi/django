from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_one(request):
    return HttpResponse("Display in App one ")



