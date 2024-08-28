from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from customers.models import Customer
from reservations.models import Reservation


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'total_products': self.page.paginator.count,
            'products_shown': len(data),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

    @action(detail=False, methods=['get'])
    def filtered(self, request):
        status = request.query_params.get('status', None)
        if status:
            self.queryset = self.queryset.filter(status=status)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            return self.get_paginated_response(self.get_serializer(page, many=True).data)
        return Response({"message": "No products found"})

    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)

            if product.status != 'available':
                return Response({"error": "Product is not available for reservation."},
                                status=status.HTTP_400_BAD_REQUEST)

            customer_id = request.data.get('customer_id')
            customer = None
            if customer_id:
                try:
                    customer = Customer.objects.get(pk=customer_id)
                except Customer.DoesNotExist:
                    return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

            Reservation.objects.create(product=product, customer=customer)

            product.status = 'reserved'
            product.save()

            return Response({"message": "Product reserved successfully."}, status=status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)