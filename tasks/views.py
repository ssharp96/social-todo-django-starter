from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'tasks/index.html')
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")