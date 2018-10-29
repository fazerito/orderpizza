from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)


    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

class Topping(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f'{self.name}'

class Pizza(models.Model):
    PIZZA_SIZES = (
        ('small', 'Small'),
        ('large', "Large")
    )
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=200, default='')
    size = models.CharField(max_length=5, choices=PIZZA_SIZES)
    stock = models.PositiveIntegerField()
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}, size: {self.size}, toppings: {self.toppings.all()}'

    def get_absolute_url(self):
        return reverse('orders:pizza_detail',
                       args=[self.id, self.slug])

class Order(models.Model):
    product_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default='')
    postal_code = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=100, default='')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='99')

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
