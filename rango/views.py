from django.shortcuts import render

from django.http import HttpResponse

def rangoIndex(request):
    return HttpResponse("Rango says: \"Hey there partner!\"")

def rangoAbout(request):
    return HttpResponse("Rango says: 'Here is the About page'")

def rangoContact(request):
    return HttpResponse("Here's how to contact us:")

def rangoLinks(request):
    return HttpResponse("Some useful links:")

