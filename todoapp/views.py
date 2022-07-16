from multiprocessing import context
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.


def index_view(request):
    # Retrieve all objects from the Task Table, order them in descending order and put into the variable 'todos'
    todos = Task.objects.all().order_by('-date_time')
    total = Task.objects.count()
    completed = 0
    current_todos = list(todos.all().filter(complete=False))

    # To count completed task based on the 'complete' boolean attributes that are True
    for x in todos:
        if (x.complete == True):
            completed = completed+1

    # To count uncompleted task based on the 'complete' boolean attributes that are False
    uncompleted = 0
    for x in todos:
        if (x.complete == False):
            uncompleted = uncompleted+1

    history_list = list(todos.filter(complete=True))

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = TaskForm()

    context = {
        'todos': todos,
        'total': total,
        'completed': completed,
        'uncompleted': uncompleted,
        'history_list': history_list,
        'current_todos': current_todos,
        'form': form,
    }
    return render(request, 'html/index.html', context)


def addtask_view(request):
    if request.method == 'POST':
        # Creating a new object of the TaskForm Class
        form = TaskForm(request.POST)
        # If the fields meet the requirements, then save the form data in db
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = TaskForm()

        context = {
            'form': form,
        }
    return render(request, 'html/index.html', context)


def edit_view(request, pk):
    current_task = Task.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=current_task)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=current_task)

    context = {
        'form': form,
    }

    return render(request, 'html/edit.html', context)


def delete_view(request, pk):
    delete_task = Task.objects.get(id=pk)

    if request.method == 'POST':
        delete_task.delete()
        return redirect('/')

    context = {
        'delete_task': delete_task
    }

    return render(request, 'html/delete.html', context)


def close_view(request, pk):
    close_task = Task.objects.get(id=pk)

    context = {
        'close_task': close_task,
    }

    if request.method == 'POST':
        close_task.complete = True
        close_task.save()
        return redirect('/')

    return render(request, 'html/close.html', context)


def clear_view(request):
    history = Task.objects.filter(complete=True)
    count_history = history.filter(complete=True).count()
    context = {
        'count_history': count_history,
    }

    if request.method == 'POST':
        history.delete()
        return redirect('/')

    return render(request, 'html/clear.html', context)
