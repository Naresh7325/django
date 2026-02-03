from django.urls import path
from . import views

urlpatterns = [
    
    path("home/",views.home),
    path("subject/",views.subject),
    path("profile/",views.profile),
    path("result",views.result),
    
    
]
