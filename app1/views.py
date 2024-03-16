# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')
def ResumePage(request):
    return render (request,'resume.html')
def FrontPage(request):
    return render (request,'frontpage.html')
def TempletPage2(request):
    return render (request,'templet2.html')
def TempletPage3(request):
    return render (request,'templet3.html')
def TempletPage(request):
    return render (request,'templetespage.html')
def TempletPage4(request):
    return render (request,'templete4.html')
def TempletPage5(request):
    return render (request,'t5.html')
def TempletPage6(request):
    return render (request,'t6.html')
def Forgetpasswordpage(request):
    return render(request,'fp.html')
def Resetpasswordpage(request):
    return render(request,'rp.html')

    
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.contrib import messages

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Your password and confirm password do not match!")
            return redirect('signup')

        # Check password constraints
        if not (len(pass1) >= 12 and any(char.isupper() for char in pass1) and any(char.isdigit() for char in pass1) and any(char.isalpha() for char in pass1) and any(char in "!@#$%^&*()-_+=<>?/:;" for char in pass1)):
            messages.error(request, "Password must be at least 12 characters long, contain at least one uppercase letter, one digit, one special character, and one letter.")
            return redirect('signup')

        # Check if username or email already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        # Create user if all conditions are met
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, "Successfully registered!")  # Set success message here
        return redirect('signup')

    return render(request, 'signup.html', {'messages': messages.get_messages(request)})





from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Username or Password is incorrect!!!'})

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
