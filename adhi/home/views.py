from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    if request.method == "POST":
        
    return render(request,"about.html")
def reg(request):
    return render(request,"login.html")