from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Blog page.</h1>")

def about(request):
    return HttpResponse("<h1>Hello, world. About page.</h1>")