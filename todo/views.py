from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import MyForm, TodoForm
from .models import Todo

# Create your views here.
def index(request):
    context = {
        'greeting': 'Hello! and welcome to Lady Pink\'s Todo List App to keep you from pulling your hair out and get you organised!!! What are you waiting for? Sign Up Below to join thousands of Pinkies in the organisation frenzy!!.',
        'message': 'Show us some love on our social media platforms, get some new inspiration on how to schedule your time effectively and get all the cool features our app has to offer.',
    }

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyForm()

    context['form'] = form

    return render(request, 'todo/index.html', context)

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('update_todo')
      
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {
        'login_form': login_form
    })

@login_required
def update_todo_view(request):
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('update_todo')
    else:
        todo_form = TodoForm()
    
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/update_todo.html', {
        'todo_form': todo_form,
        'todos': todos
    })
