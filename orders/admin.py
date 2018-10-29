from django.contrib import admin
from .models import Pizza, Topping, UserProfile


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name', 'size')}

admin.site.register(UserProfile)
admin.site.register(Topping)
admin.site.register(Pizza, PizzaAdmin)
