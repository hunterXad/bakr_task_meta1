from rest_framework import serializers
from .models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'meal', 'quantity', 'order_date', 'status', 'get_total_price']