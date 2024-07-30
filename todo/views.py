from django.shortcuts import render, redirect
from .forms import MyForm
from django.views.generic.list import ListView

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

    return render(request, 'base.html', context)


class update_todo(ListView): 
    model = Todo
    Fields = []
