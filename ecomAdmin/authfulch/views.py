from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage, get_connection
from django.conf import settings 
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        # Check if passwords match
        if password != confirm_password:
            messages.warning(request,"Password do not match")
            return render(request, 'signup.html')

        # Check if a user with the provided username or email already exists
        try:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request,"A user with this username or email already exists.")
                return render(request, 'auth/signup.html')
        except Exception as identifier:
            pass

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active=False
        user.save()
        email_subject="Activate Your Account"
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
        
    #     #Sending E-mail to the Users
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,f"Activate Your Account by clicking the link in your e-mail !") #{message}
        return redirect('/auth/login/')
    return render(request,"signup.html")
    #return redirect()  # Redirect to the user's profile page

    # return render(request, 'signup.html')
    # if request.method == "POST":
    #     email=request.POST['email']
    #     password=request.POST['pass1']
    #     confirm_password=request.POST['pass2']
    #     if password != confirm_password:
    #         messages.warning(request,"Password does not match")
    #         return render(request,'signup.html')        
    #     try:
    #         if User.objects.get(username=email):
    #             messages.info(request,"Email is taken!")
    #             return render(request,'auth/signup.html')
    #     except Exception as identifier:
    #         pass
    #     user = User.objects.create_user(email,email,password)
    #     user.is_active=False
    #     user.save()
    #     email_subject="Activate Your Account"
    #     message=render_to_string('activate.html',{
    #         'user':user,
    #         'domain':'127.0.0.1:8000',
    #         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token':generate_token.make_token(user)
    #     })
        
    # #     #Sending E-mail to the Users
    #     email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
    #     email_message.send()
    #     messages.success(request,f"Activate Your Account by clicking the link in your e-mail !") #{message}
    #     return redirect('/auth/login/')
    # return render(request,"signup.html")


#Activating The Account (Code)
class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        return render(request,'activatefail.html')



#Login Lodic
# def handlelogin(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         userpassword = request.POST['pass1']
#         myuser = authenticate(request,username=email, password=userpassword)
        
#         if myuser is not None:
#             login(request, myuser)
#             #messages.success(request,"Login Success")
#             return redirect("/")
#         else:
#             messages.error(request,"Invalid Credentials")
#             return redirect('/auth/login')
#     return render(request,"login.html")

def handlelogin(request):
    if request.method == "POST":
        email = request.POST['email']
        userpassword = request.POST['pass1']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            myuser = authenticate(request, username=user.username, password=userpassword)

            if myuser is not None:
                login(request, myuser)
                # messages.success(request, "Login Success")
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('/auth/login')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')
    return render(request, "login.html")

# Logout Function
def handlelogout(request):
    logout(request)
    messages.info(request,"Good bye. Hope to see you soon!")
    return redirect('/auth/login')


# class RequestResetEmailView(View):
#     def get(self,request):
#         return render(request,'request-reset-email.html')  
#     def post(self,request):
#         email=request.POST['email']
#         user=User.objects.filter(email=email)
#         if user.exists():
#             # current_site=get_current_site(request)
#             email_subject='[Reset Your Password]'
#             message=render_to_string('reset-user-password.html',{
#                 'domain':'127.0.0.1:8000',
#                 'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
#                 'token':PasswordResetTokenGenerator().make_token(user[0])
#             })
#             email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
#             email_message.send()
#             messages.info(request,f"WE HAVE SENT YOU A PASSWORD RESET LINK" )
#             return redirect('/auth/set-new-password/')
#         return render(request,'request-reset-email.html')
        
# class SetNewPasswordView(View):
#     def get(self,request,uidb64,token):
#         context = {
#             'uidb64':uidb64,
#             'token':token
#         }
#         try:
#             user_id=force_str(urlsafe_base64_decode(uidb64))
#             user=User.objects.get(pk=user_id)
#             if  not PasswordResetTokenGenerator().check_token(user,token):
#                 messages.warning(request,"Password Reset Link is Invalid")
#                 return render(request,'request-reset-email.html')
#         except DjangoUnicodeDecodeError as identifier:
#             pass
#         return render(request,'set-new-password.html',context)
#     def post(self,request,uidb64,token):
#         context={
#             'uidb64':uidb64,
#             'token':token
#         }
#         password=request.POST['pass1']
#         confirm_password=request.POST['pass2']
#         if password != confirm_password:
#             messages.warning(request,"Password is Not Matching")
#             return render(request,'set-new-password.html',context)        
#         try:
#             user_id=force_str(urlsafe_base64_decode(uidb64))
#             user=User.objects.get(pk=user_id)
#             user.set_password(password)
#             user.save()
#             messages.success(request,"Password Reset Success Please Login with NewPassword")
#             return redirect('/auth/login/')
#         except DjangoUnicodeDecodeError as identifier:
#             messages.error(request,"Something Went Wrong")
#             return render(request,'set-new-password.html',context)
        
#         return render(request,'set-new-password.html',context)