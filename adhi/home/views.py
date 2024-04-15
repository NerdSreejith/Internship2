from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import user_register

def index(request):
    return render(request, "index.html")

def about(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        image = request.FILES.get('img')
        password = request.POST.get('pass')
        try:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            new_user.first_name = name
            new_user.save()
            new_user_profile = user_register.objects.create(user=new_user, name=name, phone=phone)
            if image:
                new_user_profile.image = image
                new_user_profile.save()
            messages.success(request, 'User created successfully. You are now logged in.')
            login(request, new_user)
            return redirect("index")
        except Exception as e:
            return render(request, 'about.html', {'error_message': str(e)})
    else:
        return render(request, 'about.html')

def user_login(request):
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            password = request.POST.get('pass')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Invalid email or password.")
                return render(request, 'login.html')
        except Exception as e:
            print(e)
            messages.error(request, "An error occurred while processing your request.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect("index")
