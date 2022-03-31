from django.core.mail import message
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from PIL import Image
from django.db.models.deletion import CASCADE


# Create your models here.


COUNTRY_CHOICES = (
    ('India','INDIA'),
    ('Australia', 'AUSTRALIA'),
    ('New-Zeeland','NEW-ZEELAND'),
    ('Sri-Lanka','SRI-LANKA'),
    ('South-Africa','SOUTH-AFRICA'),
)
CHOICES = (
   ('S', 'Seller'),
   ('B', 'Buyer')
)
class User(AbstractUser):
    username = models.TextField(max_length=10, unique=True, null=True)
    name = models.TextField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14)
    
    # password1 = models.CharField(max_length=70, null=True)
    # password2 = models.CharField(max_length=70, null=True)
    customer = models.CharField(max_length=10, choices=CHOICES, default='Seller')
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='India')
    address = models.TextField(null=True)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=100)
    # description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='images/',null=True,blank=True,default='images/allien.png')
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=CASCADE)


    def __str__(self):
        return self.name


    

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=200)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name