from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views.task.masterTaskView import MasterTaskViewSet

route = DefaultRouter()
route.register("", MasterTaskViewSet, basename="")

task_urls = [path("", include(route.urls))]
