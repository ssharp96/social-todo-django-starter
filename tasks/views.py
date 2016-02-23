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
    
    # Instead of doing a query for all tasks here, what you want to do
    # is a search for all tasks where either a) the task is owned by the
    # current user or b) the current user is a collaborator on the task.
    # You might have to looking into Django's "Q" object for this query
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
        user = request.user
        owner = user
        title = request.POST['title']
        description = request.POST['description']
        collab_emails = []
        print("gets here 1")
        collab_emails.append(request.POST['collaborators1'].lower())
        collab_emails.append(request.POST['collaborators2'].lower())
        collab_emails.append(request.POST['collaborators3'].lower())
        print("gets here 2")
        collaborators = []
        print("gets here 3")
        # 1. Grab the collaborator emails addresses from the submitted form
        # 2. turn them into lowercase
        # 3. Look up all Users that have those email addresses
        # 4. For those that are found, make them collaborators on this new task
        # 5. Save the task
        
        is_complete = False
        task = Task(owner=owner, title=title, description=description, is_complete=False)
        if task is not None:
            task.save()
            for email in collab_emails:
                collab = User.objects.get(email=email)
                task.collaborators.add(collab)
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
                
    