from django.contrib.auth import get_user_model
from rest_framework import viewsets
from users.api.serializers import UserSerializer

Users = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
