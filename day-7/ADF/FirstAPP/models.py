from django.db import models

# Create your models here.
class Request_Info(models.Model):
    id = models.AutoField(primary_key=True)
    request_received = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode=models.IntegerField(null=True)
    qualification = models.CharField(max_length=100)
    salary = models.IntegerField(null=True)
    pan_number = models.CharField(max_length=100)
    
class Response_Info(models.Model):
    id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(Request_Info,models.DO_NOTHING,null=True)
    response = models.CharField(max_length=200)
    response_generated = models.DateTimeField(auto_now=True)
