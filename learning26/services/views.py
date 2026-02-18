from django.shortcuts import render,redirect
from .models import Service
from .forms import ServicesForm

# Create your views here.
def serviceList(request):
     service= Service.objects.all().values()
     print(service)
     return render (request,"Service/serviceList.html",{"service":service})

def createServicesWithForm(request):
    if request.method == "POST":
        form = ServicesForm(request.POST)
        if form.is_valid():          # 🔥 Ye check jaruri hai
            form.save()
            return redirect('servicelist')
    else:
        form = ServicesForm()

    return render(request, "Service/createServicesWithForm.html", {"form": form})
    
def deleteservice(request,id):
    print("id form url = ",id)
    Service.objects.filter(id=id).delete()
    return redirect("servicelist")

def updateservice(request,id):
    service=Service.objects.get(id=id)
    if request.method == "POST":
        form = ServicesForm(request.POST,instance=service)
        form.save()
        return redirect("servicelist")
    else:
        form = ServicesForm(instance=service)    
        return render(request,"Service/updateservice.html",{"form":form})

    