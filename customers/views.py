from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['get'])
    def reservations(self, request, pk=None):
        try:
            customer = self.get_object()
            reservations = Reservation.objects.filter(customer=customer)

            # TODO : transpor para logica de Background Task
            for reservation in reservations:
                if reservation.product.reservation_expiry_date and reservation.product.reservation_expiry_date < timezone.now():
                    reservation.product.status = 'available'
                    reservation.product.reservation_expiry_date = None
                    reservation.product.save()
                    reservation.delete()

            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=404)