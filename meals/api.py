from rest_framework import generics,permissions
from .models import Meals
from .serializers import MealsSerializer
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MealsFilter
from rest_framework.permissions import BasePermission

#this to check either the user is from the staff or not
class IsStaff (BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class MealsListCreateApiView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
    permission_classes = [permissions.IsAuthenticated ,IsStaff]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MealsFilter
    ordering_fields = ['name', 'price']
    ordering = ['name'] 

class MealsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
    permission_classes = [permissions.IsAuthenticated , IsStaff]