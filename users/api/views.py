from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserSerializer

Users = get_user_model()


class ListUsers(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        """get all users in the model"""
        all_users = Users.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)
