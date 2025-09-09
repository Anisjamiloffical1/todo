from django.contrib import admin
from .models import Todo, SubTask, Category, Priority
admin.site.register(Todo)
admin.site.register(SubTask)
admin.site.register(Category)
admin.site.register(Priority)

# Register your models here.
