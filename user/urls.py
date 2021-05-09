from django.contrib import admin
from django.urls import path
from user import views
from .views import userDashboard

app_name = "user"


urlpatterns = [
    path('register/',views.register,name ="register"),
    path('login/',views.loginUser,name ="login"),
    path('logout/',views.logoutUser,name ="logout"),
    path('',views.index,name="index"),
    path('dashboard/',userDashboard.as_view(),name="dashboard"),
    path('addTask/',views.addTask,name="addTask"),
    path('dashboard2/',views.testDashBoard,name="das"),


]
