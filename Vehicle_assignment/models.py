from django.db import models
from fontawesome_5.fields import IconField
from django.conf import settings
from Account.models import CustomUser
from django.utils.translation import gettext as _

# Create your models here.



class CompanyInfo(models.Model):
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15,null=True,blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField()
    adress = models.CharField(max_length=35)
    po_box = models.CharField(max_length=25)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    id = models.IntegerField(default=0,primary_key=True)

    def __str__(self) -> str:
        return self.adress

class Slider(models.Model):
    discription = models.CharField(max_length=20) 
    image = models.ImageField(upload_to="")
    id = models.IntegerField(default=0,primary_key=True)

    def __str__(self) -> str:
        return self.discription




class Vehicle(models.Model):
    model = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    image = models.ImageField(upload_to="")
    
    def __str__(self) -> str:
        return self.plate_number

    

class Service(models.Model):
    icon = IconField()
    title = models.CharField(max_length=20)
    dicription = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Abouts(models.Model):
    title = models.CharField( max_length=50)      
    description = models.TextField()  

    def __str__(self) -> str:
        return self.title

class Terms(models.Model):
    title = models.CharField( max_length=50)  
    discription = models.TextField()

    def __str__(self):
        return self.title
    
class UseOfSite(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()

    def __str__(self):
        return self.title

      
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
    

    
class Blog(models.Model):

    type = [('Pop', 'Popular'),('Per','Personal'),('LS','Life Style'),('Tech','Technical'),('Port','Portfolio')] 
    title = models.CharField(max_length=50)    
    date = models.DateTimeField( auto_now=True)
    image = models.ImageField(upload_to="")
    discription = models.TextField()
    blog_type = models.CharField( max_length=7, choices=type,null=True,blank=True)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE,null=True,blank=True)
    comment = models.IntegerField(null=True,blank=True)


    def __str__(self) -> str:
        return self.title
    
 

class Employee(models.Model):
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="")
    customuser = models.OneToOneField(CustomUser , on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.customuser.first_name

class Officer(models.Model):
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="")
    customuser = models.OneToOneField(CustomUser , on_delete=models.CASCADE)    

    def __str__(self) -> str:
        return self.customuser.first_name


class Driver(models.Model):
    vehicle = models.OneToOneField(Vehicle , on_delete=models.CASCADE)
    dob = models.DateField(null=True , blank=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="")
    avaialabilty = models.BooleanField(default=True)
    customuser = models.OneToOneField(CustomUser , on_delete=models.CASCADE,null=True,blank=True)    
   
    def __str__(self) -> str:
        return self.customuser.first_name
    



    
class Registry(models.Model):
    pick_up = models.CharField(max_length=50)
    drop_off = models.CharField(max_length=50)
    return_time = models.TimeField()
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE , null=True , blank=True                    )
    officer = models.ForeignKey(Officer , on_delete=models.CASCADE , null=True , blank=True)
    driver = models.ForeignKey(Driver , on_delete=models.CASCADE , null=True , blank=True)
    trip_description = models.TextField()
    status = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.pick_up
    

class Messages(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     email = models.EmailField()  
     phone = models.CharField(max_length=50)
     message = models.TextField()

     def __str__(self) -> str:
        return self.first_name
    


class EmployeeReview(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    comment = models.TextField()      


