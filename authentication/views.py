from login import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('home')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be less than 10 characters!")
            return redirect('home')
            
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        
        #Welcome email
        subject = "Welcome to Django login system"
        message = "Hello " + myuser.first_name +"!! \n Thank you for visiting our site \n A confirmation email has also been sent to you. \n Kindly confirm your email address \n\n Thank you" 
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
   
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)  # ✅ Fixed authentication issue

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}! You've successfully logged in.")
            return redirect('home')  # Redirect to avoid resubmitting form

        else:
            messages.error(request, "× Bad Credentials")
            return redirect('signin')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('home')
