from django.contrib import admin
from django.urls import path
from account_app.views import RegisterApi, ProfileApi

from rest_framework.routers import DefaultRouter


urlpatterns = [
      path('register', RegisterApi.as_view()),
      path('profile', ProfileApi.as_view()),
]