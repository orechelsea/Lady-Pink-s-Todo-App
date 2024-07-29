from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import MyForm

# Create your views here.
def index(request):
    context = {
        'greeting': 'Hello! and welcome to Lady Pink\'s Todo List App to keep you from pulling your hair out and get you organised!!! What are you waiting for? Sign Up Below to join thousands of Pinkies in the organisation frenzy!!.',
    }

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index')  
    else:
        form = MyForm()

   
    context['form'] = form

    return render(request, 'index.html', context)