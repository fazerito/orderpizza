from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from orders.models import Pizza
from .cart import Cart
from .forms import CartAddPizzaForm

@require_POST
def cart_add(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = CartAddPizzaForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart.add(pizza=pizza, quantity=data['quantity'], update_quantity=data['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    cart.remove(pizza)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddPizzaForm(
                          initial={'quantity': item['quantity'],
                          'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
