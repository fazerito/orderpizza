from django.contrib import admin
from .models import Pizza, Topping, User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
