import os

def populate():

# class Shows(models.Model):
#     #address break down in different model
#     #day of point of contact
#
#     directions_from_parking_to_stage = models.CharField(max_length=200)
#     parking = models.CharField(max_length=200)
#     loading_unloading_parking = models.CharField(max_length=128)
#
# class Tricks(models.Model):
#     shows = models.ForeignKey(Shows)
#     audiences = models.CharField(max_length=128)
#     props = models.CharField(max_length=128)
#     patter = models.CharField(max_length=1000)
#     cost_to_preform = models.DecimalField(max_digits= 5, decimal_places=2)
#     cost_to_buy_effect = models.DecimalField(max_digits= 5, decimal_places=2)

    # add_page(cat=python_cat,
    #     title="Official Python Tutorial",
    #     url="http://docs.python.org/2/tutorial/")
    #
    # add_page(cat=python_cat,
    #     title="How to Think like a Computer Scientist",
    #     url="http://www.greenteapress.com/thinkpython/")
    #
    # add_page(cat=python_cat,
    #     title="Learn Python in 10 Minutes",
    #     url="http://www.korokithakis.net/tutorials/python/")
    #
    # django_cat = add_cat("Django")
    #
    # add_page(cat=django_cat,
    #     title="Official Django Tutorial",
    #     url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    #
    # add_page(cat=django_cat,
    #     title="Django Rocks",
    #     url="http://www.djangorocks.com/")
    #
    # add_page(cat=django_cat,
    #     title="How to Tango with Django",
    #     url="http://www.tangowithdjango.com/")
    #
    # frame_cat = add_cat("Other Frameworks")
    #
    # add_page(cat=frame_cat,
    #     title="Bottle",
    #     url="http://bottlepy.org/docs/dev/")
    #
    # add_page(cat=frame_cat,
    #     title="Flask",
    #     url="http://flask.pocoo.org")


    # my attempt to view what is in my database
    #     shows = models.ForeignKey(Shows)
#     audiences = models.CharField(max_length=128)
#     props = models.CharField(max_length=128)
#     patter = models.CharField(max_length=1000)
#     cost_to_preform = models.DecimalField(max_digits= 5, decimal_places=2)
#     cost_to_buy_effect = models.DecimalField(max_digits= 5, decimal_places=2)



    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from lumos.models import Category, Page
    populate()
