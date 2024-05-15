import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "cycle_store_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
from cycle_store_app.models import *
# WORK BELOW

# Create

# new_customer = Customer(customer_name = 'John Smith')
# new_customer.save()

# new_customer = Customer(customer_name = 'Jane Doe')
# new_customer.save()

# new_customer = Customer(customer_name = 'Jack Fletcher')
# new_customer.save()

# new_customer = Customer(customer_name = 'John Mayer')
# new_customer.save()

# new_customer = Customer(customer_name = 'Jay Bilas')
# new_customer.save()

# Read 

customers = Customer.objects.all()
for customer in customers:
    print(customer.customer_name)

# new_vehicle_type = Vehicle(vehicle_type_bicycle = Schwin)
# new_vehicle_type.save()

#Update






