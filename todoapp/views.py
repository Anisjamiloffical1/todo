from django.shortcuts import render
from .models import *
from .forms import TodoForm, SubTaskForm, CategoryForm, PriorityForm

# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/todo_list.html', {'todos': todos})