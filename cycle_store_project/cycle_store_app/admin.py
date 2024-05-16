from django.contrib import admin
from .models import Vehicle, Customer, CustomerOrder

admin.site.register(Vehicle)
admin.site.register(Customer)
admin.site.register(CustomerOrder)

