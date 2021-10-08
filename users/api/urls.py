from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

app_name = "users"

router = DefaultRouter()

router.register("users", UsersViewSet, basename="users")

urlpatterns = []

urlpatterns += router.urls
