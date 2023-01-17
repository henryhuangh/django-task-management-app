from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateToDo
from .models import ToDos

# Create your views here.
def hello(response):
    return HttpResponse('hello world')

def todo(response):
    todos = ToDos.objects.all()
    return render(response, "todo.html", {'todos': todos})


def create_todo(response):
    add_todo = CreateToDo()
    if response.method == 'POST':
        add_todo = CreateToDo(response.POST)
        if add_todo.is_valid():
            add_todo.save()
    todos = ToDos.objects.all()
    return redirect('/todo')

def delete_todo(response, id):
    try:
        todo = ToDos.objects.get(id = id)
    except ToDos.DoesNotExist:
        redirect('/todo')
    todo.delete()
    return redirect('/todo')
