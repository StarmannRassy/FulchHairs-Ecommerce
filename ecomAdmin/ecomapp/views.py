from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from ecomapp.models import Contact,Product,OrderUpdate,Orders,Customer
from django.contrib import messages
from math import ceil
from django.db.models import Q
from ecomapp import keys
from django import forms
from django.conf import settings
from django.shortcuts import render, get_object_or_404
# from . import forms
# MERCHANT_KEY=keys.MK
import json
from django.views.decorators.csrf import  csrf_exempt
from django.views.generic.base import View
import math
import random

# from PayTm import Checksum
# from .models import Payment
# from django.shortcuts import get_object_or_404


# Create your views here.
# Loading products into the Frontend   
def index(request):
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request,"index.html",params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        phonenumber = request.POST.get("phonenumber")
        myquery = Contact( 
            name=name,
            email=email,
            desc=desc,
            phoneNumber=phonenumber,
        )
        myquery.save()
        messages.info(request,"We will get back to you shortly...")
        return render(request,"contact.html")
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def payment(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login') 
    
    user = request.user
    address, created = Customer.objects.get_or_create(user=user)
    # order, created = Orders.objects.filter(user=user)

    if request.method == 'POST':

        address.locality = request.POST['locality']
        address.city = request.POST['city']
        address.state = request.POST['state']
        address.zipcode = request.POST['zipcode']
        address.country = request.POST['country']
        address.mobile = request.POST['mobile']
        address.save()

        messages.success(request, "Address Updated Successfully")
        return redirect('address')
        # 
    
    # if request.method=="POST":
    #     items_json = request.POST.get('itemsJson', '')
    #     amount = request.POST.get("payment.amount")
    #     O_id = "FH" + math.ceil(random(1,45248))/2 + math.floor(random(2000, 457877))/3 + 1
    #      # Use filter to retrieve all orders for the current user
    #     orders = Orders.objects.filter(user=user)

    #     # Process each order
    #     for order in orders:
    #         # Update the order's attributes
    #         order.items_json = items_json
    #         order.amount = amount
    #         order.oid = O_id
    #         # order.amountpaid = amount
    #         order.save()
    #         return redirect('/orders')

    return render(request, 'payment.html', {'user': user, 'address': address})
    return render(request,"payment.html")


def ordersp(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    


    return render(request,"orders.html")


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    return render(request,"checkout.html") 


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    user = request.user

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # phone_number = request.POST['phone_number']

        # Update the user's profile information
        user.first_name = first_name
        user.last_name = last_name
        # user.phone_number = phone_number
        user.save()

    return render(request, 'profile.html', {'user': user})



def address(request):
    user = request.user
    address, created = Customer.objects.get_or_create(user=user)

    if request.method == 'POST':

        address.locality = request.POST['locality']
        address.city = request.POST['city']
        address.state = request.POST['state']
        address.zipcode = request.POST['zipcode']
        address.country = request.POST['country']
        address.mobile = request.POST['mobile']
        address.save()

        messages.success(request, "Address Updated Successfully")
        return redirect('address')

    return render(request, 'address.html', {'user': user, 'address': address})
    return render(request, 'address.html')

