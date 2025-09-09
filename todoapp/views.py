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