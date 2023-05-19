
from django.contrib import admin
from django.urls import path,include
# adamya
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
# from api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api_app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),        # adamya
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),       # adamya
  
]
