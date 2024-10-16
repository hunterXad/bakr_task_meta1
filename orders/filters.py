# filters.py
import django_filters
from .models import Orders

class OrdersFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='icontains')
    order_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Orders
        fields = ['status', 'order_date']
