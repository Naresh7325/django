from django.shortcuts import render,redirect
from .models import Service
from .forms import servicesform
def home(request):
    return render(request, "student/home.html")

def subject(request):
    return render(request, "student/subject.html")

def profile(request):
    return render(request,"student/profile.html")

def result(request):
    return render(request,"student/result.html")


def serviceList(request):
    services=Service.objects.all()
    return render (request,"student/servicelist.html",{"services":services})

def createservice(request):
    if request.method == "POST":
        form = servicesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = servicesform()
        return render(request,"student/createService.html",{"form":form})

def Deleteservice(request,id):
    def Deleteservice(request,id):
     print("id form url = ",id)
    Service.objects.filter(id=id).delete()
    return redirect("serviceList")

        


