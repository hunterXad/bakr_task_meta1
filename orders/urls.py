from django.urls import path
from . import views
from .api import OrderListCreateView,OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('new/', views.order_create, name='order_create'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'), 
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail')
]

