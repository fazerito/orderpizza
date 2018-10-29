from decimal import Decimal
from django.conf import settings
from orders.models import Pizza


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, pizza, quantity=1, update_quantity=False):
        pizza_id = str(pizza.id)
        if pizza_id not in self.cart:
            self.cart[pizza_id] = {'quantity': 0, 'price': str(pizza.price)}
        if update_quantity:
            self.cart[pizza_id]['quantity'] = quantity
        else:
            self.cart[pizza_id]['quantity'] += quantity

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, pizza):
        pizza_id = str(pizza.id)
        if pizza_id in self.cart:
            del self.cart[pizza_id]
            self.save()

    def __iter__(self):
        pizza_ids = self.cart.keys()
        pizzas = Pizza.objects.filter(id__in=pizza_ids)
        for pizza in pizzas:
            self.cart[str(pizza.id)]['pizza'] = pizza

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
