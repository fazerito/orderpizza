from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def index(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")

def about(request):
    return render(request, "orders/about.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, "orders/register_form.html", args)
