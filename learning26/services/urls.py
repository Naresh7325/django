from django.urls import path
from . import views   # ✅ VERY IMPORTANT

app_name = "services"


urlpatterns = [
    path('serviceList/', views.serviceList, name="servicelist"),
    path('createServiceWithForm/', views.createServicesWithForm, name="createServiceWithForm"),
    path('deleteservice/<int:id>/',views.deleteservice,name="deleteservice"),
    path('updatesevice/<int:id>/',views.updateservice,name="updateservice"),


]
