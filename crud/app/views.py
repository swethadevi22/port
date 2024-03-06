from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import reg
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
def home(request):
    my=reg.objects.all()
    if(my!=""):
        return render(request,"home.html",{"reg":my})
    else:
        return render(request,"home.html")

def add(request):
    if request.method=="POST":
        n=request.POST["name"]
        a=request.POST["age"]
        e=request.POST["email"]

        obj=reg()
        obj.Name=n
        obj.Age=a
        obj.Email=e
        obj.save()
        my=reg.objects.all()
        return redirect("home")
    return render(request,"home.html")

def update(request,id):
    my=reg.objects.get(id=id)
    if request.method=="POST":
        n=request.POST["name"]
        a=request.POST["age"]
        e=request.POST["email"]
        my.Name=n
        my.Age=a
        my.Email=e
        my.save()
        return redirect("home")
    return render(request,"update.html",{"data":my})

def delete(request,id):
    my=reg.objects.get(id=id)
    my.delete()
    return redirect("home")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log innow!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

