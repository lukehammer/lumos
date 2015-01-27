from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold fount "}
    return render(request,"lumosmagic/index.html", context_dict)

# Create your views here.
