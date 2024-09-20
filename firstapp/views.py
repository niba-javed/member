from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from firstapp.models import Welcome
# Create your views here.

def welcome(request):
    users = Welcome.objects.all().values()

    template = loader.get_template('hello.html')
    context = { 
        'user' : users,
    }
    return HttpResponse(template.render(context,request                      ))