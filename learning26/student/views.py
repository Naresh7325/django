from django.shortcuts import render

def home(request):
    return render(request, "student/home.html")

def subject(request):
    return render(request, "student/subject.html")

def profile(request):
    return render(request,"student/profile.html")

def result(request):
    return render(request,"student/result.html")
