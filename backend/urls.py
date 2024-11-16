from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import login_view, register_view, get_current_user, get_user_by_id



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('api/user/', get_current_user, name='get-user'),
    path('api/auth/register/', register_view, name='register'),
    path('api/auth/login/', login_view, name='login'),
    path('api/users/<int:pk>/', get_user_by_id, name='user-detail'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('rentals.urls')),
    path('api/', include('payment.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
