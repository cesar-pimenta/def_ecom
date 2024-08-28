from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'reservation_date')
    search_fields = ('product__name', 'customer__name')
    list_filter = ('reservation_date',)