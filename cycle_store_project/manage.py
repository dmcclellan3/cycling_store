#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cycle_store_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    ## VEHICLE CRUD

def create_vehicle(vehicle_type, number_in_stock):
    vehicle = vehicle(type =vehicle_type, number_in_stock=number_in_stock)
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

def create_customer(name):
    customer = Customer(name=name)
    customer.save()
    print(f"Created customer: {customer}")

def read_customers():
    customers = Customer.objects.all()
    for customer in customers:
        print(customer)