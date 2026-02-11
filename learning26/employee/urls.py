
from . import views
from django.urls import path
urlpatterns = [
    path('employeelist/', views.employeelist),
    path('employeefilter/',views.employeefilter),
    path('createEmployeeWithForm/',views.createEmployeeWithForm),
    path('createcourse',views.createcourse),
    path('createmovie',views.createmovie),
    path('createteam/',views.createteam),

]