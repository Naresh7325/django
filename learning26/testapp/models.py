from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('CUSTOMER', 'Customer'),
        ('STAFF', 'Service Staff'),
    )

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="User"

    def __str__(self):
        return f"{self.username} ({self.role})"


class Admin(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)#foregin key
    admin_level = models.CharField(max_length=50)  # Super, Manager, etc.

    class Meta:
        db_table="Admin"

    def __str__(self):
        return self.userId.username


class ServiceStaff(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    designation = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    salary = models.IntegerField()

    class Meta:
        db_table="ServiceStaff"

    def __str__(self):
        return self.userId.username
    
class Customer(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Customer"

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
    customerId= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    vehicle_color=models.CharField(max_length=100)
    vehicle_model=models.CharField(max_length=100)

    class Meta:
        db_table="Vehicle"

    def __str__(self):
        return self.vehicle_number

class Documentation(models.Model):
    vehicleId= models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='documents')
    doc_type = models.CharField(max_length=50)
    doc_file = models.FileField(upload_to='documents/')
    doc_number=models.CharField(max_length=100)
    expiry_date=models.DateField()

    class Meta:
        db_table="Documetation"

class ParkingDetails(models.Model):
    vehicleId= models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    parking_slot = models.CharField(max_length=50)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)
    daily_charge = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "parking_details"

    def __str__(self):
        return f"{self.vehicleId} - {self.parking_slot}"

class ServiceDetail(models.Model):
    vehicleId= models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='services')
    staffId= models.ForeignKey(ServiceStaff, on_delete=models.SET_NULL, null=True, related_name='services')
    service_type = models.CharField(max_length=100)
    service_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        db_table="ServiceDetail"

class Transportation(models.Model):
    vehicleId= models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='transportations')
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    date = models.DateField()


    class Meta:
        db_table="Transportation"

class Payment(models.Model):
    customerId= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payments')
    serviceId= models.OneToOneField(ServiceDetail, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table="Payment"




