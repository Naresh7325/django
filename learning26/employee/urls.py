
from . import views
from django.urls import path
urlpatterns = [
    path('employeelist/', views.employeelist,name="employeelist"),
    path('employeefilter/',views.employeefilter),
    path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
    path('createcourse',views.createcourse),
    path('createmovie',views.createmovie),
    path('createteam/',views.createteam),
    path("deleteemployee/<int:id>",views.deleteemployee,name="deleteemployee"),
    path("filteremployee/",views.filteremployee,name="filteremployee"),
    path("sortemployee/<int:id>",views.sortemployee,name="sortemployee")



]