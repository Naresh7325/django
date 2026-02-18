from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userlist/',views.userlist,name="userlist"),
    path('createUserForm/',views.createUserForm,name="createUserForm"),
    
]
