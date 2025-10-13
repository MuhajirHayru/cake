from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Item1(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    discription=models.TextField()

    def __str__(self):
        return self.name



class About(models.Model):
    
    profilepic=models.ImageField(upload_to='items1/')
    about=models.TextField()
    aboutmyself=models.TextField(null=True)
    email=models.EmailField(blank=True)
    location=models.CharField( max_length=200,null=True)
    worktime=models.TextField(null=True,blank=True)
    phoneNo =PhoneNumberField(unique=True)
    telegramlink=models.TextField()
    video = models.FileField(upload_to='videos/',null=True,blank=True) 
    def __str__(self):
        return self.email
class special(models.Model):
    specialname=models.CharField(max_length=500,null=True)
    ingridents=models.CharField(max_length=500)
    price=models.IntegerField()
    extrabenefit=models.CharField( max_length=500)
    def __str__(self):
        return self.ingridents
class Category(models.Model):
    Cname=models.CharField(max_length=100 ,null=True,default='all')
    def __str__(self):
        return self.Cname
class Gallaryy(models.Model):
    catagory=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='img1/')
    gallaryname=models.CharField( max_length=500)
    uploded_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.gallaryname
    

    

   

    

  