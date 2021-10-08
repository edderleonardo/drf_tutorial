from django.contrib.auth import get_user_model
from django.http import Http404
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

    def post(self, request):
        """create a new user"""
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


class UsersDetails(APIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Get user detail"""
        user = self.get_object(pk)
        serializers = UserSerializer(user)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializers = UserSerializer(user, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
