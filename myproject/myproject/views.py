#from django.http import HttpResponse 
from django.shortcuts import render

def homepage(request):
   # return HttpResponse("Hello World! I'm Home.")
   return render(request, 'home.html')

def about(request):
    #return HttpResponse("My About Page.")
     return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def team(request):
    return render(request, 'team.html')