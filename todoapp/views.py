from django.shortcuts import render, redirect
from .models import *
from .forms import TodoForm, SubTaskForm, CategoryForm, PriorityForm

# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todoapp/create_todo.html', {'form': form})

def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoapp/update_todo.html', {'form': form})

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todoapp/delete_todo.html', {"todo": todo})
