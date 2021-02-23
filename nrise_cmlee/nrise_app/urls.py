from django.urls import path, include
from nrise_app.views import (
	UserAPIView,
)

urlpatterns = [
	path("api/user", UserAPIView.as_view(), name="user_create"),
]
