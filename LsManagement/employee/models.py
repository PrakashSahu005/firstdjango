from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "employee"


class EmployeeDetail(models.Model): 
    eid = models.CharField(max_length=20)  
    eDob = models.CharField(max_length=100)  
    eGender = models.EmailField()
    eAddress = models.CharField(max_length=254)
    eJoiningDate = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    class Meta:  
        db_table = "employeeDetail"