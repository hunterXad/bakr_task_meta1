from rest_framework import generics, permissions
from .models import Orders
from .serializers import OrderSerializer
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OrdersFilter

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OrdersFilter
    ordering_fields = ['order_date', 'status']
    ordering = ['order_date'] 

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]