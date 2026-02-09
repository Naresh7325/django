from django.contrib import admin
from .models import User, Admin,Customer,ServiceStaff,Vehicle,Documentation,ParkingDetails,ServiceDetail,Transportation,Payment

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Vehicle)
admin.site.register(Documentation)
admin.site.register(ParkingDetails)
admin.site.register(ServiceDetail)
admin.site.register(Transportation)
admin.site.register(Payment)


