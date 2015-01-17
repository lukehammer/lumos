from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
from lumos.models import Show, Person



def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    show_list = Show.objects.order_by('name')
    person_list = Person.objects.order_by("first_name")


    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!


    context_dict = {'boldmessage': "I am bold font from the context",
                    "lukes_message": "Hello I'm the text that Luke is writing to prove that i understand where stuff comes from.",
                    "shows": show_list,
                    "persons": person_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('lumos/index.html', context_dict, context)

def monkeys(request):
    return render_to_response('lumos/about.html')

def show(request):
    #render('suck it')
    return HttpResponse('suck it trebek')

def ajax(request):

    if request.method == "POST":
        category = Category()
        category.name = request.POST["name"]
        category.save()

    category_list = list(Category.objects.all())

    test_list = []
    for ii in category_list:
        test_list.append({
            "name":ii.name,
            })

    return HttpResponse(dumps(test_list), content_type='application/json')