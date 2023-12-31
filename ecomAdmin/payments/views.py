from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Payment, UserWallet
from django.conf import settings
from django.contrib import messages
from ecomapp.models import Orders,OrderUpdate

def initiate_payment(request):
    user = request.user
    orders = Orders.objects.filter(user=user)
    # Process each order
    for order in orders:
        if request.method == "POST":      
            amount = request.POST['amount']
            # Update the order's attributes
            order.amountpaid = amount
            order.save()
        
        # updates = OrderUpdate.objects.create()
        
        # for update in updates:
        #     update.update_desc="Order placed successfully.",
        #     update.delivered=False
    
        #     update.save()
            
    if request.method == "POST":      
        amount = request.POST['amount']
        email = request.POST['email']
        pk = settings.PAYSTACK_PUBLIC_KEY
        payment = Payment.objects.create(amount=amount, email=email, user=request.user)
        payment.save()
        context = {
            'payment': payment,
            'field_values': request.POST,
            'paystack_pub_key': pk,
            'amount_value': payment.amount_value(),
        }
        return render(request, 'make_payment.html', context)  
       
        # return render(request, 'make_payment.html', context)        
    return render(request, 'checkout.html')


def verify_payment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()

    # if verified:
    #     user_wallet = UserWallet.objects.get(user=request.user)
    #     user_wallet.balance += payment.amount
    #     user_wallet.save()
    # print(request.user.username, )
    messages.success(request,"Payment made Successfully")
    return render(request, "success.html")
    return render(request, "success.html")
