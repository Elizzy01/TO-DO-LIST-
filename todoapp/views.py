from django.shortcuts import render
from .models import TodoApp

# Create your views here.

def homepage(request):
    if request.method=="POST":
        name=request.POST["name"]
        try:
            completed=request.POST["completed"]
        except:
            completed=False
        if completed == 'on':
            todoapp=TodoApp.objects.create(name=name,completed=True)
        else:
            todoapp=TodoApp.objects.create(name=name)
    todoapp=TodoApp.objects.all()
    return render(request, "index.html", {"todolist":todoapp})
