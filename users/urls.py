from django.urls import path
from .views import login_view, register_view, get_current_user, get_user_by_id
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/', get_current_user, name='get-user'),
    path('auth/register/', register_view, name='register'),
    path('auth/login/', login_view, name='login'),
    path('users/<int:pk>/', get_user_by_id, name='user-detail'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
