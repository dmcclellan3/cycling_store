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

# customers = Customer.objects.all()
# for customer in customers:
#     print(customer.customer_name)

 ## VEHICLE CRUD

def create_vehicle(vehicle_type, number_in_stock):
    vehicle = vehicle(type=vehicle_type, number_in_stock=number_in_stock)
    vehicle.save()
    print(f"Created Vehicle: {vehicle}")

def read_vehicle():
    vehicles = vehicle.objects.all()
    for vehicle in vehicles:
        print(vehicle)

def update_vehicle(vehicle_id, vehicle_type=None, number_in_stock=None):
    try: 
        vehicle = vehicle.objects.get(id=vehicle_id)
        if vehicle_type:
            vehicle.type = vehicle_type
        if number_in_stock is not None:
            vehicle.number_in_stock = number_in_stock
        vehicle.save()
        print(f"Update Vehicle: {vehicle}")
    except vehicle.DoesNotExist:
        print("Vehicle Not Found")

def delete_vehicle(vehicle_id):
    try:
        vehicle = vehicle.objects.get(vehicle_id)
        vehicle.delete()
        print(f"Deleted Vehicle: {vehicle}")
    except vehicle.DoesNotExist:
        print("Vehicle Not Found")

        ## Customer CRUD

def create_customer():
    name = input("Enter Name")
    customer = Customer(customer_name=name)
    customer.save()
    print(f"Created customer: {customer}")

# create_customer('Jane Doe')

def read_customers():
    customers = Customer.objects.all()
    for customer in customers:
        print(customer)


def update_customer(customer_id, name):
    try: 
        customer = Customer.objects.get(id=customer_id)
        customer.customer_name = name
        customer.save()
        print(f"Updated Customer: {customer}")
    except Customer.DoesNotExist:
        print(f"Customer Not Found")

# update_customer(4, 'John Jacobs')

def delete_customer(customer_id, name):
    try: 
        customer = Customer.objects.get(id=customer_id)
        customer.customer_name = name
        customer.delete()
        print(f"Customer Deleted: {customer}")
    except Customer.DoesNotExist:
        print(f"Customer Not Found")

    ## Customer Order CRUD 

# delete_customer(2, 'Jane Doe')
# read_customers()

def create_order(customer):
    try: 
        # customer = Customer.objects.get(id=customer_id)
        order = CustomerOrder(customer=customer)
        order.save()
        for vehicle in Vehicle.objects.all():
            print(f'{vehicle.id} - {vehicle}')
        sel_id = input('Enter ID of Vehicle ')
        sel_vehicle = Vehicle.objects.get(id=sel_id)
        order.order.add(sel_vehicle)
        order.save()
        print(f"Order Created {order}")
    except Customer.DoesNotExist:
        print("Customer Not Found")
    except Vehicle.DoesNotExist:
        print("Vehicle Not Found")

# customer = Customer.objects.get(id=7)
# create_order(customer)

def read_orders():
    orders = CustomerOrder.objects.all()
    for order in orders:
        print(order)

# read_orders()


def update_order(order_id, customer_id=None, vehicle_ids=None, paid=None):
    try:
        order = CustomerOrder.objects.get(id=order_id)
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
            order.customer = customer
        if vehicle_ids is not None:
            order.order.clear()
            for vehicle_id in vehicle_ids:
                vehicle = Vehicle.objects.get(id=vehicle_id)
                order.order.add(vehicle)
        if paid is not None:
            order.paid = paid
        order.save()
        print(f"Updated order: {order}")
    except CustomerOrder.DoesNotExist:
        print("Order not found")
    except Customer.DoesNotExist:
        print("Customer not found")
    except Vehicle.DoesNotExist:
        print("Vehicle not found")

def delete_order(order_id):
    try:
        order = CustomerOrder.objects.get(id=order_id)
        order.delete()
        print(f"Deleted order: {order}")
    except CustomerOrder.DoesNotExist:
        print("Order not found")


##Vehicle CRUD

def create_vehicle():
    try:
        vehicle_type = input("Enter Type ")
        vehicle = Vehicle(type=vehicle_type, number_in_stock=1)
        vehicle.save()
        print(f"Created Vehicle: {vehicle}")
    except Vehicle.DoesNotExist:
        print('Vehicle Not Found')

# create_vehicle('bicycle')

def read_vehicle():
    vehicle = Vehicle.objects.all()
    for vehicle in vehicle:
        print(vehicle)


def update_vehicle(type):
    try: 
        vehicle = Vehicle.objects.filter(type=type).first()
        vehicle.number_in_stock = vehicle.number_in_stock + 1
        vehicle.save()
        print(f"Updated Vehicle: {vehicle}")
    except Vehicle.DoesNotExist:
        print(f"Vehicle Not Found")

# update_vehicle('bicycle')

def delete_vehicle(type):
    try: 
        vehicle = Vehicle.objects.filter(type=type).first()
        vehicle.delete()
        print(f"Vehicle Deleted: {vehicle}")
    except Vehicle.DoesNotExist:
        print(f"Vehicle Not Found")
 
def run_program():
    ## List of vehicles
    print(f'\
          \n \
          The Duke of Cycles \n \
          \n \
          ***************** \n \
          1 - List Vehicles \n \
          2 - List Customers \n \
          3 - List Orders \n \
          4 - New Customer \n \
          5 - Create Vehicle \n \
          Q - Quit \n \
          ')
    choice = input("Select Option and Hit <ENTER> ")
    if choice == 'Q' or choice == 'q':
        quit()
    elif choice == '1':
        read_vehicle()
    elif choice == '2':
        read_customers()
    elif choice == '3':
        read_orders()
    elif choice == '4':
        create_customer()
    elif choice == '5':
        create_vehicle()
    ## List of customers
    ## List of orders
    ## add customer
    ## add order

run_program()








