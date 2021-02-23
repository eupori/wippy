from django.urls import path, include
from .yasg import *
from nrise_app.views import (
	UserAPIView,
	SessionAPIView,
	UserDetailAPIView,
)

urlpatterns = [
	path("api/user", UserAPIView.as_view(), name="user"),
	path("api/user/<int:id>", UserDetailAPIView.as_view(), name="user-detail"),
	path("api/session/<int:id>", SessionAPIView.as_view(), name="session"),
	path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
