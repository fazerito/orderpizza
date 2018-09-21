from django.contrib import admin
from .models import Pizza, Topping, UserProfile
from django.contrib.auth.admin import UserAdmin


admin.site.register(UserProfile)
admin.site.register(Pizza)
admin.site.register(Topping)
