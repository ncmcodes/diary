"""
URL configuration for diary project.
"""

from django.contrib import admin
from django.urls import path, include
from diaryAPI.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("diaryAPI.urls")),
    path("", index),
]
