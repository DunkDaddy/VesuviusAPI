from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customers)
admin.site.register(Location)
admin.site.register(Tables)
admin.site.register(Reservation)
admin.site.register(Category)
admin.site.register(Ingredients)
admin.site.register(MenuItems)
admin.site.register(Itemassembly)
admin.site.register(OrderItems)
admin.site.register(Order)
admin.site.register(Table_list)

