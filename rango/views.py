from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: \"Hey there partner!\"")

def about(request):
    return HttpResponse("Rango says: 'Here is the About page'")

def contact(request):
    return HttpResponse("Here's how to contact us:")

def links(request):
    return HttpResponse("Some useful links:")

