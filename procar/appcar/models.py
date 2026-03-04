from django.db import models

# Create your models here.

class userregisterpage(models.Model):
    username=models.CharField(max_length=20)
    useremail=models.EmailField(max_length=30)
    userphone=models.IntegerField()
    userimg=models.ImageField(upload_to='images/')
    userpass=models.CharField(max_length=15)
    def __str__(self):
        return self.username
    
class carregistrationpage(models.Model):
    carimg=models.ImageField(upload_to='images/')
    carname=models.CharField(max_length=35)
    cardesc=models.CharField(max_length=800)
    carprice=models.IntegerField()
    carcate=models.CharField(max_length=200)
    caryear=models.IntegerField(default=0)
    carmonth=models.CharField(max_length=10,default='none')
    carmodel=models.CharField(max_length=15,default='none')
    caralter=models.CharField(max_length=10, default='none')
    carcolor=models.CharField(max_length=15,default='none')
    carfuel=models.CharField(max_length=20,default='none')
    carversion=models.CharField(max_length=20,default='none')
    carowner=models.CharField(max_length=20,default='none')
    carkilo=models.IntegerField(default=0)
    def __str__(self):
        return self.carname
    
class wishitemcar(models.Model):
    userid=models.IntegerField()
    item=models.ForeignKey(carregistrationpage,on_delete=models.CASCADE)
    
