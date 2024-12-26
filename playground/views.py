from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    return HttpResponse('Hello world')

def render_response(request):
    # return render(request, 'hello.html', {"name": "Shameem"})
    x = 1
    y = 2
    return render(request, 'hello.html', {})