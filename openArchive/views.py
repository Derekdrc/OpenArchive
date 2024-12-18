#from django.http import HttpResponse
#Django tutorial and Derek D'Arcy
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello world")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("About")
    return render(request, 'about.html')