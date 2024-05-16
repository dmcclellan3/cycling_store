from django.db import models

# Create your models here.

    
class Vehicle(models.Model):
    vehicle_types = [
        ('unicycle', 'Unicycle'),
        ('bicycle', 'Bicycle'),
        ('tricycle', 'Tricycle'),
    ]

    type = models.CharField(max_length=100, choices=vehicle_types, default='bicycle')
    number_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.get_type_display()} ({self.number_in_stock} in stock)"
    

class Customer(models.Model):
    customer_name = models.TextField(max_length=100)

    def __str__(self):
        return self.customer_name
    
class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ManyToManyField(Vehicle)
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
    