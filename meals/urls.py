from django.urls import path
from .views import MealsListView, MealsDetailView, MealsCreateView, MealsUpdateView, MealsDeleteView
from .api import MealsListCreateApiView , MealsDetailApiView

urlpatterns = [
    path('list/', MealsListView.as_view(), name='meals_list'),   
    path('<int:pk>/', MealsDetailView.as_view(), name='meals_detail'),  
    path('create/', MealsCreateView.as_view(), name='meals_create'),
    path('update/<int:pk>/', MealsUpdateView.as_view(), name='meals_update'),
    path('delete/<int:pk>/', MealsDeleteView.as_view(), name='meals_delete'),

    path('api/meals/', MealsListCreateApiView.as_view(), name='meals-list-create'),
    path('api/meals/<int:pk>/', MealsDetailApiView.as_view(), name='meals-detaill'),
]