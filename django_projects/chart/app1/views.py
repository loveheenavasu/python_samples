import re
from django.shortcuts import render,redirect
from .forms import ProForm, Signupform
from django.contrib import messages
from .models import Product, UserUniqueToken
from django.contrib.auth.models import User
import secrets,hashlib
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout as django_logout, login as auth_login
# Create your views here.
def createuser(request):
    if request.method=="POST":
        form=Signupform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            print(username)
            form.save()
            salt = secrets.token_hex(8) 
            token = hashlib.sha256(salt.encode('utf-8')).hexdigest()
            user_id = User.objects.get(username=username)
            token_updated, token_created = UserUniqueToken.objects.update_or_create(user_id=user_id, defaults={"token": token})
            messages.success(request,'Account created successfully') 
            return redirect("login") 
    else:
        form=Signupform()
    return render(request,"signup.html",{'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = auth_login(request,user)
          
            return redirect("profile")
        else:
            messages.info(request,'invalid username or password')     
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def profile(request):
    if request.user.is_authenticated:
        pro=Product.objects.all()
        if request.method=="POST":
            obj=ProForm(request.POST)
            if obj.is_valid():
                obj.save()
        else:
            obj=ProForm()

        return render(request,"profile.html",{'pro':pro,'obj':obj})
    else:
        return redirect("login")

def logout(request):
    django_logout(request)
    return redirect("login")

def signup(request):
    return render(request,"signup.html") 


