from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from tasks.models import *

# Create your views here.

def tasks(request):
    tasks = Task.objects.all()
    current_user = request.user
    # tasks[] = 
    # for task in all_tasks:
    #     if task.owner == current_user:
            
        
    if current_user.is_authenticated():
        template = loader.get_template('tasks/tasks.html')
        context = {'tasks': tasks}
        return render(request, "tasks/tasks.html", {'context': context})
    else:
        print("what the fuck am i doing here?")
        return HttpResponseRedirect('/')
    
# def create(request):
    
    