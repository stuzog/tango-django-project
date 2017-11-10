from django.shortcuts import render
from rango.models import Category, Page


def rangoindex(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by number of likes in descending order.
    # Retrieve the top five only, or all if less than five.
    # Replace the list on our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


# def rangoindex(request):
#     # Construct a dictionary to pass to the template engine as its context
#     # Note that the key boldmessage is the same as {{ boldmessage }}
#     # in the template!
#     context_dict = {'boldmessage': "Get some crunchy, creamy, cookie, candy, cupcake!"}
#
#     # Return a rendered response to send to the client.
#     # We make use of the shortcut function to make our lives easier.
#     # Note that the first parameter is the template we wish to use.
#     return render(request, 'rango/index.html', context=context_dict)
#

def rangoabout(request):
    # return HttpResponse("Rango says: \"Here is the About page\"")
    context_dict = {'boldmessage': "About Rango we know very little."}

    return render(request, 'rango/about.html', context=context_dict)


def rangolinks(request):
    # return HttpResponse("Some useful links:")
    context_dict = {'boldmessage': "Here are some useful links"}

    return render(request, 'rango/links.html', context=context_dict)


def rangofiles(request):
    # return HttpResponse("Files you can download and use")
    context_dict = {'boldmessage': "Here are some useful files"}

    return render(request, 'rango/files.html', context=context_dict)


def rangocontact(request):
    # return HttpResponse("Here's how to contact us:")
    context_dict = {'boldmessage': "Here's how to contact us"}

    return render(request, 'rango/contact.html', context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary that we can pass to the template engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or raise an exception.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
