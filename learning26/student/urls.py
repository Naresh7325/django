from django.urls import path
from . import views


urlpatterns = [
    
    path("home/",views.home),
    path("subject/",views.subject),
    path("profile/",views.profile),
    path("result",views.result),
    path("serviceList/",views.serviceList,name="serviceList"),
    path("createservice/",views.createservice,name="createservice"),
    path("Deleteservice/<int:id>/",views.Deleteservice,name="Deleteservice"),
    

    
]
