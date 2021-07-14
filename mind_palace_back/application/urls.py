from django.urls import path
from rest_framework.routers import DefaultRouter

from mind_palace_back.application import views


router = DefaultRouter()


urlpatterns = [
    path('enums', views.EnumsApiView.as_view())
]