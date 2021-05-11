from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("/")

    content = {'tasks':tasks, 'form':form}
    return render(request, 'list.html', content)


def edit(request, idx):
    task = Task.objects.get(id=idx)
    form = TaskForm(instance=task)
    content = {'form' : form}

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'edit.html', content)

def delete(request, idx):
    task = Task.objects.get(id=idx)
    task.delete()

    return redirect("/")
