from django.urls import path

from .views import ListUsers

app_name = "users"

urlpatterns = [
    path('users/list/', ListUsers.as_view(), name="users_list")
]
