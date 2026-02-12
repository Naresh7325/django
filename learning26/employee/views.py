from django.shortcuts import render,HttpResponse,redirect 
from .models import Employee
from .forms import EmployeeForm,CourseForm,MovieForm,TeamForm

# Create your views here.
def employeelist(request):
     employees = Employee.objects.all().values()
     print(employees)
     return render (request,"employee/employeelist.html",{"employees":employees})

def employeefilter(request):
    #where select  from employee where name = "raj"
    employee = Employee.objects.filter(name ="naresh").values()
    #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="Developer").values()
    #select  from employee where name = "raj" and post = "Developer"
    employee3 = Employee.objects.filter(name ="sunil",post ="Developer").values()
    #select  from employee where name = "raj" or post = "Developer"

    #>23
    #seelct  from employee where age > 23
    #employee4 = Employee.objects.filter(age>23).values()
    employee4 = Employee.objects.filter(age__gt=20).values()
    employee5 = Employee.objects.filter(age__gte=20).values()

    #lt , lte

    #string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()
    #contains
    employee8 = Employee.objects.filter(name__contains="s").values()
    employee9 = Employee.objects.filter(name__icontains="S").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="S").values()
    employee11 = Employee.objects.filter(name__endswith="S").values()
    employee12 = Employee.objects.filter(name__istartswith="S").values()
    employee13 = Employee.objects.filter(name__iendswith="S").values()

    #in
    employee14 = Employee.objects.filter(name__in=["naresh","sunil"]).values()    

    #range
    employee15 = Employee.objects.filter(age__range=[21,25]).values()    

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc

    

    #and
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
#     return render(request, 'employee/employeeFilter.html')  
    return render(request,"employee/employeefilter.html", 
                   {"query1":employee,
                    "query2":employee2,
                    "query3":employee3,
                    "query4":employee4,
                    "query5":employee5,
                    "query17":employee17,

                    })
def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() #it same as create
        # return HttpResponse("EMPLOYEE CREATED...")
        return redirect("employeelist")
    else:
        #form object create --> html
        form = EmployeeForm() #form object        
        return render(request,"employee/createEmployeeForm.html",{"form":form})

def createcourse(request):
    print(request.method)
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save()
        return HttpResponse("COURSE CREATED...")
    else:
        form= CourseForm()
        return render (request, "employee/createcourse.html",{"form":form})
        
def createmovie(request):
    print(request.method)
    if request.method == "POST":
        form=MovieForm(request.POST)
        form.save()
        return HttpResponse("movie store...")
    else:
        form = MovieForm()
        return render (request,"employee/createmovie.html",{"form":form})
    
def createteam(request):
    print(request.method)
    if request.method == "POST":
        form=TeamForm(request.POST)
        form.save()
        return HttpResponse("team create ....")
    else:
        form=TeamForm()
        return render(request,"employee/createteam.html",{"form":form})

def deleteemployee(request,id):
    print("id from url = ",id)
    Employee.objects.filter(id=id).delete()
    return redirect("employeelist")

def filteremployee(request):
    print("filter employee called ...")
    employee=Employee.objects.filter(age__gte=50).values()
    print("filter employees =  ",employee)
    return render (request,"employee/employeelist.html",{"employees":employee})

def sortemployee(request,id):
      if id==1:
          employee = Employee.objects.order_by("age").values()
  
      elif id==2:
          employee = Employee.objects.order_by("-age").values()
          
      else:
           employees = Employee.objects.all().values()

      return render (request,"employee/employeelist.html",{"employees":employee})


