from django.contrib import admin
from django.urls import path, include
from todo.urls.userUrls import user_urls
from todo.urls.taskUrls import task_urls
from todo.urls.taskTypeUrls import task_type_urls
from todo.views.auth.customTokenObtainPairView import CustomTokenObtainPairView
from todo.views.auth.customTokenBlacklistView import CustomTokenBlacklistView
from todo.views.auth.customTokenRefreshView import CustomTokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("auth/blacklist/", CustomTokenBlacklistView.as_view(), name="token_blacklist"),
    path("users/", include(user_urls)),
    path("tasks/", include(task_urls)),
    path("task_type/", include(task_type_urls)),
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="SAMU API",
        default_version="Beta",
    ),
    public=True,
    permission_classes=[IsAdminUser],
    authentication_classes=[SessionAuthentication],
)

urlpatterns += [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
