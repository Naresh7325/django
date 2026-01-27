from django.http import HttpResponse
from django.shortcuts import render

def test():
    return HttpResponse ("Hello")

def Aboutus(request):
    return render(request,"aboutus.html")

def Contectus(request):
    return render(request,"contectus.html")

def Home(request):
    return render(request,"home.html")

def Movies(request):
    return render(request,"movies.html")

def Shows(request):
    return render(request,"shows.html")

def News(request):
    return render(request,"news.html")