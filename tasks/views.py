from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from tasks.models import *
from splash.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import models

# Create your views here.

def tasks(request):
    all_tasks = Task.objects.all()
    current_user = request.user
    tasks = []
    for task in all_tasks:
        if task.owner == current_user or task.collaborators == current_user.email:
            tasks.append(task)
    if current_user.is_authenticated():
        # template = loader.get_template('tasks/tasks.html')
        context = {'tasks': tasks}
        return render(request, "tasks/tasks.html", {'context': context})
    else:
        return HttpResponseRedirect('/')
    
def create(request):
    if request.method == 'POST':
        print("gets here 1")
        user = request.user
        owner = user
        title = request.POST['title']
        description = request.POST['description']
        # collaborators = request.POST['confirm_password']
        is_complete = False
        print("gets here 2")
        task = Task(owner=owner, title=title, description=description, is_complete=False)
        print("gets here 3")
        if task is not None:
            task.save()
            return HttpResponseRedirect('/tasks/')
        else:
            return render(request, 'tasks/tasks.html', {'errors':"Make sure you fill in all forms!"})

def delete(request, task_id):
    task_id = int(task_id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/tasks/')
    
def toggle(request, task_id):
    task_id = int(task_id)

    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.is_complete == True:
            task.is_complete = False
        else:
            task.is_complete = True

        task.save();
    return HttpResponseRedirect('/tasks')
                
    