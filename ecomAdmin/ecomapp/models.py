from django.db import models
from django.contrib.auth.models import User
# import secrets
# from .paystack import Paystack

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phoneNumber = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)   
    image = models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0) 
    oid = models.CharField(max_length=150, blank=True)
    amountpaid = models.CharField(max_length=500, blank=True, null=True)
    paymentstatus = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.order_id)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField()
    zipcode = models.CharField(max_length=10, null=False)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Nigeria")
    
    def __str__(self):
        return self.user.username