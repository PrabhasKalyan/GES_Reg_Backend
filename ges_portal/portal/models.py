from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import uuid
from django.contrib.auth.models import AbstractUser

class Users(User):
    phone_number=models.CharField(max_length=15)
    roles=[
        ("Student","Student"),
        ("CA","CA"),
        ("Professional","Professional"),
        ("Contingent","Contingent "),
        ("Startup","Startup"),
    ]
    role=models.CharField(max_length=24,choices=roles)
    payment_status = models.BooleanField(default=False)
    ca_code = models.CharField(max_length=6,blank=True,null=True)
    ges_id = models.CharField(max_length=10, unique=True, blank=True,default=f'GES{uuid.uuid4().hex[:4].upper()}')

    sizes=[
        ("S","S"),
        ("M","M"),
        ("L","L"),
        ("XL","XL"),
        ("XXL","XXL"),
    ]
    shirt_size = models.CharField(max_length=24,choices=sizes,blank=True,null=True)
    arrival_date = models.DateField(blank=True,null=True)
    departure_date = models.DateField(blank=True,null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contingent(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    insti=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    no_of_people=models.PositiveIntegerField()
    def __str__(self):
        return self.insti

class Professional(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    proffession = models.CharField(max_length=256)
    industry = models.CharField(max_length=256)
    years_of_experience = models.PositiveIntegerField()
    curr_org = models.CharField(max_length=256)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Startup(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    startup_name = models.CharField(max_length=256)
    industry = models.CharField(max_length=256)
    year_of_establishment = models.PositiveIntegerField( validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year), ],)
    stages=[
        ("Preseed","Preseed"),
        ("Seed","Seed"),
        ("Funding","Funding")
    ]
    stage_of_startup = models.CharField(max_length=100,choices=stages)
    if_ic = models.BooleanField(default=True)
    cofounders = models.CharField(max_length=256)
    def __str__(self):
        return self.startup_name
        
class Student(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    insti = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5), ])
    dept = models.CharField(max_length=256)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



class CA(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    insti = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5), ])
    dept = models.CharField(max_length=256)
    no_of_regs = models.PositiveIntegerField(default=0)
    registered_users = models.ManyToManyField(Users, related_name="referral_cas",default=None)
    link = models.URLField(blank=True,null=True,default="")
    referral_code = models.CharField(
        max_length=4, 
        unique=True, 
        default=str(uuid.uuid4())[:4],
    )
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"  



