from django.contrib import admin
from django.urls import path, include
from .views import task_create_or_list_view

urlpatterns = [
    path('', task_create_or_list_view),
]
