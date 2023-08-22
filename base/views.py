from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.getAllTasks()

    context = {'tasks':tasks}
    return render(request, 'base/home.html', context)

def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = TaskForm()

    context = {'form':form}
    return render(request, 'base/task_form.html', context)
