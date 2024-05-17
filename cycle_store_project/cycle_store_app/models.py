from django.db import models

# Create your models here.

    
class Vehicle(models.Model):


    type = models.CharField(max_length=100, default='bicycle')
    number_in_stock = models.PositiveIntegerField(1)

    def __str__(self):
        return f"{self.type} ({self.number_in_stock} in stock)"
    

class Customer(models.Model):
    customer_name = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.customer_name}"
    
class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_order', null=True)
    order = models.ManyToManyField(Vehicle)
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.customer_name}"
    