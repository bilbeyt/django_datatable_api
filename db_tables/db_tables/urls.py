from django.contrib import admin
from django.urls import path, include
from user_api.views import HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path('admin/', admin.site.urls),
    path("api/", include("user_api.urls"))
]
