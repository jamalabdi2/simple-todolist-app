from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.http import HttpResponseRedirect


def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed = True)
    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks
        }

    print(tasks)
    print(completed_tasks)
  
    return render(request,'home-todo1.html',context)

def create_task(request):
    task = request.POST['task'] 
    Task.objects.create(task=task)
    print(request.POST['task'])
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task,id=pk) 
    if request.method =='POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        print(new_task)
        return redirect('home')
    context = {'get_task':get_task}
    return render(request,'todos/edit_task.html',context)

def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')


