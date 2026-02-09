# from django.db import models

# # Create your models here.
#     #new table 
# class student(models.Model):
#     studentName=models.CharField(max_length=100)
#     studentAge=models.IntegerField()
#     studentCity=models.CharField(max_length=100)
#     studentEmail=models.EmailField(null=True)

#     #meta 
#     class Meta:
#         db_table='student' #table name 

#     def __str__(self):
#         return self.studentName
#     #new table 
# class product(models.Model):
#     productName=models.CharField(max_length=100)
#     productPrice=models.IntegerField()
#     productDescription=models.CharField(max_length=50)
#     productStock=models.PositiveIntegerField()
#     productColor=models.CharField(max_length=50,null=True)
#     productStatus=models.BooleanField(default=True)

#     class Meta :
#         db_table='product' 

#     #new table 
# class sportItem(models.Model):
#     sportitemName=models.CharField(max_length=100)
#     sportitemPrice=models.IntegerField()
#     sportitemDescription=models.CharField(max_length=100)
#     sportitemQuntity=models.IntegerField()
#     sportitemColor=models.CharField(max_length=100,null=True)

#     class Meta:
#         db_table='sportitem'

  
      
# class studentProfile(models.Model):
#         hobbies=(('reading','reading'),('travel','travel'),('music','music'))

#         studentId=models.OneToOneField(student,on_delete=models.CASCADE)
#         studentHobbies=models.CharField(max_length=100,choices=hobbies)
#         studentAddress=models.CharField(max_length=100)
#         studentPhone=models.CharField(max_length=100)
#         studentGender=models.CharField(max_length=100)
#         studentDOB=models.DateField()

#         class Meta:
#             db_table='studentProfile'

#         def __str__(self):
#             return self.studentId.studentName    

# class category(models.Model):
#     categoryName=models.CharField(max_length=100)
#     categoryDescription=models.TextField()
#     categoryStatus=models.BooleanField(default=True)

#     class Meta:
#         db_table="category"

#     def __str__(self):
#         return self.categoryName

# class service(models.Model):
#     serviceName=models.CharField(max_length=100)
#     serviceDescription=models.TextField()
#     servicePrice=models.IntegerField()
#     serviceStatus=models.BooleanField(default=True)
#     discount=models.IntegerField(null=True)
#     categoryId=models.ForeignKey(category,on_delete=models.CASCADE)
#     class Meta:
#         db_table="service"

#     def __str__(self):
#         return self.serviceName
    
# class user(models.Model):
#     userName=models.CharField(max_length=100)
#     userAge=models.IntegerField()
#     userEmail=models.EmailField(null=True)
#     userPhone=models.CharField(max_length=100)

#     class Meta:
#         db_table="user"

#     def __str__(self):
#         return self.userName
    
# class bankdetail(models.Model):
#     accountName=models.CharField(max_length=100)
#     accountNumber=models.TextField()
#     accountType=models.CharField(max_length=100)
#     ifscCode=models.TextField()
#     userId=models.OneToOneField("user",on_delete=models.CASCADE)

#     class Meta:
#         db_table="bankdetail"

#     def __str__(self):
#         return self.accountName
    
# class client(models.Model):
#     clientName=models.CharField(max_length=100)
#     clientage=models.IntegerField()
#     clientCity=models.CharField(max_length=100)
#     clientEmail=models.EmailField(null=True)

#     class Meta:
#         db_table="client"

#     def __str__(self):
#         return self.clientName 

# class car(models.Model):
#     carName=models.CharField(max_length=100)
#     carCompany=models.CharField(max_length=100)
#     carPrice=models.IntegerField()
#     carmodel=models.TextField()
#     cardeatils=models.CharField(max_length=100)
#     clientId=models.ForeignKey(client,on_delete=models.CASCADE)

#     class Meta:
#         db_table="car"

#     def __str__(self):
#         return self.carName 
    
# class person(models.Model):
#     personName=models.CharField(max_length=100)
#     personAge=models.IntegerField()
#     personEmail=models.EmailField(null=True)

#     class Meta:
#         db_table="person"

#     def __str__(self):
#         return self.personName
    
# class Bike(models.Model):
#     BikeName=models.CharField(max_length=100)
#     BikeikeCompany=models.CharField(max_length=100)
#     BikeikePrice=models.IntegerField()
#     Bikeikemodel=models.TextField()
#     Bikeikedeatils=models.CharField(max_length=100)
#     personId=models.ForeignKey(person,on_delete=models.CASCADE)

#     class Meta:
#         db_table="Bike"

#     def __str__(self):
#         return self.BikeName