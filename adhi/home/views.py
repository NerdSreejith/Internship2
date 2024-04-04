from django.shortcuts import render,HttpResponse,redirect
from .models import user_register
from django.contrib.auth.models import  User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        image = request.FILES.get('img')
        password =  request.POST.get('pass')
        print(name,password)
        new_user = user_register(name= name,email =email,phone = phone,image= image,password = password)
        new_user.save()
        return redirect("index")

    return render(request,"about.html")
def reg(request):
    return render(request,"login.html")