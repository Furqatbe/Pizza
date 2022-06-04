from distutils.command.upload import upload
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField
from rest_framework.authtoken.models import Token
# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=123)
    text = models.TextField()
    img = models.ImageField(upload_to = 'Slider/')

class Info(models.Model):
    phone = models.IntegerField()
    location =  models.CharField(max_length=123)
    day_time = models.DateTimeField()
    tw = models.URLField()
    fb = models.URLField()
    insta = models.URLField()


class Welcome_text(models.Model):
    title = models.CharField(max_length=123)
    text  = models.TextField()
    img = models.ImageField(upload_to = 'Slider/')

class Service(models.Model):
    icon = models.ImageField(upload_to = 'Service/')
    name = models.CharField(max_length=123)
    text =  models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=123)
    text = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField(Category)
    img = models.ImageField(upload_to  = 'Product/')

    def __str__(self):
        return self.name

class Achievment(models.Model):
    logo = models.ImageField(upload_to = 'Achieviment/')
    number = models.IntegerField()
    name = models.CharField(max_length=123)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.product.name





class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Blog(models.Model):
    img = models.ImageField(upload_to = 'Blog/')
    name = models.CharField(max_length=123)
    text = models.TextField()
    category = models.ManyToManyField(Category)


class Contact(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    massege = models.TextField()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()

#     def __str__(self):
#         return self.product.name