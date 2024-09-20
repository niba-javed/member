from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from members.models import Welcome

def members(request):
    users = Welcome.objects.all().values()
    template = loader.get_template('members.html')
    context={
        'users': users,
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    user= Welcome.objects.get(id=id)
    template = loader.get_template('details.html')
    context={
        'user':user,
    }
    return HttpResponse(template.render(context,request))



def main (request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing (request):
    mydata = Welcome.objects.all().order_by('id')
    template = loader.get_template('template.html')
    context = {
        'mymembers':mydata,
    }
    return HttpResponse(template.render(context,request)) 