from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world, New django project")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world, New django  about page")


def contact(request):
    return HttpResponse("Hello, world, New django contact page")


