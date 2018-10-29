from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Pizza
from cart.forms import CartAddPizzaForm

def index(request):
    return render(request, "orders/index.html")

def menu(request):
    pizzas = Pizza.objects.all()
    return render(request, "orders/menu.html", {'pizzas': pizzas})

def pizza_detail(request, id, slug):
    pizza = get_object_or_404(Pizza, id=id, slug=slug)
    cart_product_form = CartAddPizzaForm()
    args = {
        'pizza': pizza,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'orders/pizza_detail.html', args)

def about(request):
    return render(request, "orders/about.html")

def register(request):
    registered = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
    else:
        form = RegistrationForm()
    args = {'form': form,
            'registered': registered}
    return render(request, "orders/register_form.html", args)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'orders/index.html')
            else:
                return HttpResponse('Your account has been disabled.')
        else:
            return HttpResponse('Bad credentials.')
    return render(request, "orders/login.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('index'))
