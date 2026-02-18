from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.
def home(request):
    return render(request, "testapp/home.html")

def userlist(request):
    users=User.objects.all()
    print(users)
    return render (request,"testapp/userlist.html",{"users":users})

def createUserForm(request):
    print(request.method)
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save() #it same as create
        # return HttpResponse("EMPLOYEE CREATED...")
        return redirect("userlist")
    else:
        #form object create --> html
        form = UserForm() #form object        
        return render(request,"testapp/createUserForm.html",{"form":form})