from multiprocessing import context
from django.shortcuts import render,redirect

# Create your views here.
# from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm



def home(request):
    todos= Todo.objects.all()
    # home kısmında post methodunu yapabilmek için formu context e koyup home.html e gönderdik ve form yapısını home.html e ekledik.
    form = TodoForm()
    context={
        "form":form,
        "todos":todos
    }
    return render(request,"todo/home.html",context)

def todo_create(request):
    form=TodoForm
    if request.method== "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        "form":form
    }
    return render(request,"todo/todo_add.html",context)

def todo_update(request,id):
    todo =Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

    context={
        # "todo":todo,
        "form":form
    }
    return render(request,"todo/todo_update.html",context)
