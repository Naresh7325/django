from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name=models.CharField(max_length=100)
    fees=models.IntegerField()
    duration=models.IntegerField()

    class Meta:
        db_table="course"

    def __str__(self):
        return self.name 

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    publishyear=models.IntegerField()

    class Meta:
        db_table="movie"

    def __str__(self):
        return self.name 
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    sports=models.CharField(max_length=100)

    class Meta:
        db_table="team"

    def __str__(self):
        return self.name 
