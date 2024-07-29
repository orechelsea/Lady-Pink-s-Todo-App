from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import MyForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyForm()
    return render(request, "index.html", {"form": form})