from django.shortcuts import render
from django.http import HttpResponse

def display_two(request):
    return HttpResponse("Display in app 2")
# Create your views here.
