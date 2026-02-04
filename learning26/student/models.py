from django.db import models

# Create your models here.
    #new table 
class student(models.Model):
    studentName=models.CharField(max_length=100)
    studentAge=models.IntegerField()
    studentCity=models.CharField(max_length=100)
    studentEmail=models.EmailField(null=True)

    #meta 
    class meta:
        db_table='student' #table name 

    #new table 
class product(models.Model):
    productName=models.CharField(max_length=100)
    productPrice=models.IntegerField()
    productDescription=models.CharField(max_length=50)
    productStock=models.PositiveIntegerField()
    productColor=models.CharField(max_length=50,null=True)
    productStatus=models.BooleanField(default=True)

    class meta :
        db_table='product' 

    #new table 
class sportItem(models.Model):
    sportitemName=models.CharField(max_length=100)
    sportitemPrice=models.IntegerField()
    sportitemDescription=models.CharField(max_length=100)
    sportitemQuntity=models.IntegerField()
    sportitemColor=models.CharField(max_length=100,null=True)

    class meta:
        db_table='sportitem'