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
