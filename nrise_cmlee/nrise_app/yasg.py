from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from drf_yasg import openapi

schema_url_patterns = [
	path('/', include('nrise_app.urls')),
] 

schema_view = get_schema_view(
    openapi.Info(
        title='엔라이즈 프로젝트 API',
        default_version='v1.0',
        description=
        '''
        엔라이즈 테스트용 API 문서 페이지입니다.
        ''',
        terms_of_service="https://www.google.com/policies/terms/"
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)