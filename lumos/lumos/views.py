from django.http import HttpResponse

def index(resuest):
    return HttpResponse("lumos says hello world!")