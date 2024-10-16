import django_filters
from .models import Meals

class MealsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter()
    available = django_filters.BooleanFilter()

    class Meta:
        model = Meals
        fields = ['name', 'price', 'available']