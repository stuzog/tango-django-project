from django.shortcuts import render

from django.http import HttpResponse


def rangoIndex(request):

    # Construct a dictionary to pass to the template engine as its context
    # Note that the key boldmessage is the same as {{ boldmessage }}
    # in the template!
    context_dict = {'boldmessage': "Get some crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)


def rangoAbout(request):

   # return HttpResponse("Rango says: \"Here is the About page\"")
    context_dict = {'boldmessage': "About Rango we know very little."}

    return render(request, 'rango/about.html', context=context_dict)


def rangoLinks(request):
    # return HttpResponse("Some useful links:")
    context_dict = {'boldmessage': "Here are some useful links"}

    return render(request, 'rango/links.html', context=context_dict)


def rangoFiles(request):
    # return HttpResponse("Files you can download and use")
    context_dict = {'boldmessage': "Here are some useful files"}

    return render(request, 'rango/files.html', context=context_dict)


def rangoContact(request):
    # return HttpResponse("Here's how to contact us:")
    context_dict = {'boldmessage': "Here's how to contact us"}

    return render(request, 'rango/contact.html', context=context_dict)


