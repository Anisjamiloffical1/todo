from django import forms
from .models import Category, Priority, Todo, SubTask


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['level']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'category', 'priority', 'due_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'completed']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subtask'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }