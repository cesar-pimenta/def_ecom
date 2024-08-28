from django.db import models


class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('unavailable', 'Unavailable')
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

    def reserve(self):
        if self.status == 'available':
            self.status = 'reserved'
            self.save()
            return True
        return False
