from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)


    def __str__(self):
        return f'{self.first_name}  {self.last_name}, {self.address} {self.city}, ZIP CODE: {self.zip_code}'

class Topping(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Pizza(models.Model):
    PIZZA_SIZES = (
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', "Large")
    )
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Topping)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}, size: {self.size}, toppings: {self.toppings.all()}'

class Order(models.Model):
    product_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total_cost = models.IntegerField()
