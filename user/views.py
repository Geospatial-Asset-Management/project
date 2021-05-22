from django.shortcuts import render,redirect
from  .forms import UserRegisterForm
from .forms import LoginForm
from user import models
from django.views.generic import ListView
from crt_ast.models import Asset
from .forms import TaskForm
from Task.models import Task
from crt_ast.views import AssetTable
from Task.views import TaskTable
from crt_ast.views import PointTable
from crt_ast.models import Point



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

            return redirect("index")
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


def addTask(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        

        form.save()
        
        return redirect("index")
    return render (request,"addTask.html",{"form":form})


def testDashBoard(request):
    context = {}
    context['table_assets'] = AssetTable(Asset.objects.all())
    context['table_tasks'] = TaskTable(Task.objects.filter(assigned_to=request.user))
    return render(request,"dashboard.html",context)

class userDashboard(ListView):
    model = Asset
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_assets"] = AssetTable(Asset.objects.all())
        context["table_tasks"] = TaskTable(Task.objects.all())
        context["table_points"] = PointTable(Point.objects.all())
        return context
    
    



def tasklist(request):


    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render (request,"tasklist.html",context)
    


