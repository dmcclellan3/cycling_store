from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.TextField(max_length=100)

    def __str__(self):
        return self.customer_name
    
class Vehicle(models.Model):
    vehicle_type_bicycle = models.TextField(max_length=100)
    vehicle_type_tricycle = models.TextField(max_length=100)
    vehicle_type_unicycle = models.TextField(max_length=100)
    number_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return (f"Bicycle: {self.vehicle_type_bicycle}, "
                f"Tricycle: {self.vehicle_type_tricycle}, "
                f"Unicycle: {self.vehicle_type_unicycle}, "
                f"Number in stock: {self.number_in_stock}")

    