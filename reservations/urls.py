from django.urls import path
from . import views
from .api import ReservationListCreateView,ReservationRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.template, name='template'),
    path('list/', views.list_reservations, name='reservation_list'),  
    path('new/', views.create_reservation, name='create_reservation'),  
    path('<int:pk>/edit/', views.update_reservation, name='update_reservation'), 
    path('<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),
    path('api/reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'), 
    path('api/reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail')
  
]
