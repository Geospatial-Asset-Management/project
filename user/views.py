from django.shortcuts import render,redirect
from  .forms import UserRegisterForm
from .forms import LoginForm
from user import models
from django.views.generic import ListView
from crt_ast.models import Asset



from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.

def register (request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data.get('username')
            name = form.cleaned_data.get('first_name')
            
            messages.success(request,"Basariyla kayit oldunuz")

            return redirect("dashboard")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)


    else:
        form = UserRegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context)



def loginUser (request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"kullanici adi veya parola hatali")
            return render(request,"login.html",context)

        messages.success(request,"basariyla giris yaptiniz")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)


def logoutUser (request):
    logout(request)
    return redirect("index")

def index(request):
    return render(request,"index.html")

def deneme(request):
    return render(request,"a.html")

def userRegister(request):
    return render(request,"register.html")




class userDashboard(ListView):
    model = Asset
    template_name = 'dashboard.html'
    fields = ('name')


