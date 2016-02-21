from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    template = loader.get_template('tasks/index.html')
    context = {'tasks': tasks,}
    return HttpResponse(template.render(context, request))
    
# def create(request, request.session['username']):
#     var current_user = request.session['username]
    