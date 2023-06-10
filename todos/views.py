from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponseRedirect

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    context = {'tasks':tasks}

    print(tasks)
  
    return render(request,'home-todo1.html',context)

def create_task(request):
    task = request.POST['task'] 
    Task.objects.create(task=task)
    print(request.POST['task'])
    return redirect('home')





