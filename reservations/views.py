from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reservation
from .serializers import ReservationSerializer
from products.models import Product
from customers.models import Customer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        customer_id = request.data.get('customer_id')
        customer = Customer.objects.get(id=customer_id)

        if product.reserve():
            Reservation.objects.create(customer=customer, product=product)
            return Response({'status': 'Product reserved'}, status=status.HTTP_200_OK)
        return Response({'status': 'Reservation failed'}, status=status.HTTP_400_BAD_REQUEST)
