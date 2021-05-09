"""asset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, draw
from geo.views import cesiumAsset
from user import views
from crt_ast.views import AssetListView
from crt_ast.views import CreateAsset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #view.py def adı
    path('home/', home_view, name='home'),
    path('assets/', cesiumAsset),
    path('user/',include("user.urls")),
    path('welcome/',views.deneme,name="a"),
    path('user/register',views.userRegister,name='reg'), 
    path('user/logout',views.logoutUser,name='logout'), 
    path('user/login',views.loginUser,name ='login'),
    path('draw/', draw , name='draw'),
    path('deneme/', AssetListView.as_view()),
    path('task/', views.tasklist,name = 'tasklist'),
    path('crt_asset/', CreateAsset),


]
