from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views.user.masterUserView import MasterUserViewSet

route = DefaultRouter()
route.register('', MasterUserViewSet, basename='')

user_urls = [
    path('', include(route.urls))
]