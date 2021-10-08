from django.urls import path

from .views import ListUsers, UsersDetails

app_name = "users"

urlpatterns = [
    path('users/list/', ListUsers.as_view(), name="users_list"),
    path('users/list/<int:pk>', UsersDetails.as_view(), name="users_detail")
]
