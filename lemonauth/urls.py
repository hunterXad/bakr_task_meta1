from django.urls import path
from .views import SignupView , HomeView , LogunView ,CustomLogoutViews
from django.contrib.auth import views as auth_views
from .api import RegisterView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LogunView.as_view(), name='login'),
    path('logout/', CustomLogoutViews.as_view(), name='logout'),
    
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='loginn'),
    path('api/logout/', LogoutView.as_view(), name='logoutt'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
]
