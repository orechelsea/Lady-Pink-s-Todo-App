from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/form submitted successfully/")
    else:
        form = MyForm()
    return render(request, "index.html", {"form": form})