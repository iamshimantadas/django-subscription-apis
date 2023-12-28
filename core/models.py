from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import PermissionsMixin

from core.manager import UserManager

class Carousel(models.Model):
    img1 = models.ImageField(upload_to="media/core")
    img2 = models.ImageField(upload_to="media/core")
    img3 = models.ImageField(upload_to="media/core")
    descp = models.TextField()


class AboutUs(models.Model):
    heading = models.CharField(max_length=200)
    thumbimg = models.ImageField(upload_to="media/core")
    about_descp = models.TextField()

class WhyChooseUs(models.Model):
    choose_heading1 = models.CharField(max_length=250)
    chooose_descp1 = models.TextField()
    choose_heading2 = models.CharField(max_length=250)
    chooose_descp2 = models.TextField()
    choose_heading3 = models.CharField(max_length=250)
    chooose_descp3 = models.TextField()

class ContactUs(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()

# custom model    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=200, unique=True)
    address = models.TextField(null=True)
    phone = models.BigIntegerField()
    profile = models.ImageField(upload_to="media/core")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
    

