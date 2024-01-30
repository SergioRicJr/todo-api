from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views.task_type.masterTaskTypeView import MasterTaskTypeViewSet

route = DefaultRouter()
route.register('', MasterTaskTypeViewSet, basename='')

task_type_urls = [
    path('', include(route.urls))
]