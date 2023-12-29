from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import PermissionsMixin

from core.manager import UserManager

class Carousel(models.Model):
    carousel_heading = models.CharField(max_length=200)
    carousel_img = models.ImageField(upload_to="media/core",null=True)
    carousel_desc = models.TextField()
    
    def __str__(self):
        return self.carousel_heading

class AboutUs(models.Model):
    heading = models.CharField(max_length=200)
    thumbimg = models.ImageField(upload_to="media/core")
    about_descp = models.TextField()

class WhyChooseUs(models.Model):
    chooseus_heading = models.CharField(max_length=250)
    chooseus_descp = models.TextField()
    

class ContactUs(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()

class OurTeam(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    profileimg = models.ImageField(upload_to="media/core", null=True)

    def __str__(self):
        return self.name

# custom model    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=200, unique=True)
    address = models.TextField(null=True)
    phone = models.BigIntegerField(null=True)
    profile = models.ImageField(upload_to="media/core",null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
    

