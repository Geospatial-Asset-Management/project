from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #html kodu çalıştırmak için

from django.template import loader

def home_view(request): #home page create

    template = loader.get_template('home.html')
    context = {
    }
    
    return HttpResponse(template.render(context, request))