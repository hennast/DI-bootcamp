from django.shortcuts import render # this line is added automatically

# Create your views here.
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return render(request, "myapp/template/hello.html", {})