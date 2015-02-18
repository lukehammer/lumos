from django.shortcuts import render
from django.http import HttpResponse
from json import dumps, loads
from django.views.decorators.csrf import csrf_exempt
from lumosmagic.models import Trick

<<<<<<< HEAD
def show_builder(request):
    trick_list = Trick.objects.order_by('name')
    context_dict = {"tricks": trick_list}
    return render(request, 'lumosmagic/show_builder.html', context_dict)
=======
>>>>>>> 28be70440ac8e95134e156a58c485c17c13e226e





<<<<<<< HEAD
def navagation(request):
    context_dict = {}
    return render(request,"lumosmagic/navagation.html", context_dict)
=======

>>>>>>> 28be70440ac8e95134e156a58c485c17c13e226e


def index(request):
    context_dict = {'boldmessage': "I am bold fount "}
    return render(request,"lumosmagic/index.html", context_dict)

def trick(request):
    context_dict = {}
    return render(request,"lumosmagic/tricks.html", context_dict)

# Create your views here.

#this is a example for people editing forms
def dom(request):
    if request.method == "POST":
        print request.POST
    return render(request, 'lumosmagic/dom.html')

<<<<<<< HEAD
=======
def show_builder(request):
    if request.method == "POST":
        print request.POST
    return render(request, 'lumosmagic/show_builder.html')
>>>>>>> 28be70440ac8e95134e156a58c485c17c13e226e

@csrf_exempt
def ajax(request):

    if request.method == "POST":
        trick = Trick()
        trick.name = request.POST["trickName"]
        trick.length = request.POST["trickLength"]
        trick.save()

<<<<<<< HEAD

=======
>>>>>>> 28be70440ac8e95134e156a58c485c17c13e226e
    trick_list = list(Trick.objects.all())

    test_list = []
    for ii in trick_list:
        test_list.append({
            "name":ii.name,
            "length":ii.length,
            })

    return HttpResponse(dumps(test_list), content_type='application/json')
