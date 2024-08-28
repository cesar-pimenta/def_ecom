from django.db import models
from django.utils import timezone
from customers.models import Customer
from products.models import Product
from datetime import timedelta


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        customer_name = self.customer.name if self.customer else "No Customer"
        return f"Reservation for {self.product.name} by {customer_name}"

    def has_expired(self):
        return timezone.now() > self.reservation_date + timedelta(days=3)

    def expire(self):
        self.product.status = 'available'
        self.product.save()
        self.delete()