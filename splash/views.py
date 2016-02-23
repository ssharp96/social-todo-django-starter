from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import models
from tasks.models import Task, User
from django.contrib.auth.models import User
from tasks import views
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    # tasks = Task.objects.all()
    # template = loader.get_template('tasks/index.html')
    # context = {'tasks': tasks,}
    # return HttpResponse(template.render(context, request))
    return render(request, 'splash/index.html')
    
    
def login_view(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return render(request, "tasks/tasks.html")
                return HttpResponseRedirect('/tasks/')
            else:
                return HttpResponse("Oops! Something went wrong!")
        
        else:
          return HttpResponse("Incorrect username or password! Go back and try again!")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def register_view(request):
    username = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    name = []
    name = username.split(' ')
    first_name = name[0]
    last_name = name[1]

    u = User.objects.create_user(username=email, first_name = first_name, last_name = last_name, email = email, password = password)
    u = authenticate(username=email, email=email, password=password)
    login(request, u)

    if u is not None:
        if password != confirm_password:
            return render(request, "index.html", {'errors':"Passwords don't match."})
        else:
            u.save()
            return HttpResponseRedirect('/tasks/')
    else:
        return render(request, "index.html" , {'errors': "Ensure you fill in all the fields"})

    return HttpResponseRedirect('/tasks/')
    
    
    