import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    # First, we will create a list of dictionaries containing the pages
    # we want to add in each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little confusing, but it allows us to iterate
    # through each data structure, and add data to our models.

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think Like A Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python In 10 Minutes",
         "url": "http://korokithakis.net/tutorials/python"}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djamgoproject.com/en/1.11/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://djangorocks.com/"},
        {"title": "How To Tango With Djngo",
         "url": "http://www.tangowithdjango.com/"}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"},
        {"title": "VicPiMakers Meetup",
         "url": "https://www.meetup.com/Victoria-Raspberry-PiMakers-And-Others/"}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # If you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information abut how to iterate properly over a dictionary.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

        # Print out the categories we have added.
        for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views, likes=likes)[0]
    p.cat = cat
    p.title = title
    p.url = url
    p.views = views
    p.likes = likes
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
