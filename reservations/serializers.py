from rest_framework import serializers
from .models import Reservation
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer

class ReservationSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'
