from django.urls import path
from user_api.views import CustomUserAPIView


urlpatterns = [
    path("users/", CustomUserAPIView.as_view(), name="users")
]
