from django.shortcuts import render,redirect
from  .forms import RegisterForm
from .forms import LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register (request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username =username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            messages.success(request,"Basariyla kayit oldunuz")

            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)


    else:
        form = RegisterForm()
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
    messages.success(request,"başarıyla çıkış yaptınız")
    return redirect("index")

def index(request):
    return render(request,"index.html",context={"myvar":"Deneme"})
