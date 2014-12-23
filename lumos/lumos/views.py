from django.http import HttpResponse

def index(resuest):
    return HttpResponse("lumos says hello world!")
def monkeys(resuest):
    return HttpResponse("the monkeys are after you")