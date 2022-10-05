from django.shortcuts import render, redirect
from todos.forms import TodoForm
from .models import Todos

# Create your views here.
def index(request):
    Todo_lists = Todos.objects.all()
    context = {
        'Todo_lists': Todo_lists,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('todos:index')
    else:
        todo_form = TodoForm()
    context = {
        'todo_form_': todo_form,
    }
    return render(request, 'todos/create.html', context)

def detail(request, pk):
    todo = Todos.objects.get(id=pk)
    context = {
        'todo': todo,
        'todo_title': todo.title,
        'todo_content': todo.content,
    }
    return render(request, 'todos/detail.html', context)

def delete(request, pk):
    todo_del = Todos.objects.get(id=pk)
    todo_del.delete()
    return redirect('todos:index')

def update(request, pk):
    todo_update = Todos.objects.get(id=pk)
    if request.method == 'POST':
        todo_form = TodoForm(request.POST, instance=todo_update)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('todos:detail', pk)
    else:
        todo_form = TodoForm(instance=todo_update)

    context = {
        'todo_form': todo_form,
    }

    return  render(request, 'todos/update.html', context)