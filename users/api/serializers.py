from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'total_fortune',
        ]


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'profile',
        ]

    def validate_email(self, email):
        email_domain = email.split('@')[1]

        if email_domain == 'yahoo.com':
            raise serializers.ValidationError(
                "No permitimos el registro con una cuenta de Yahoo")
        return email

    def create(self, validate_data):
        profile = validate_data.pop('profile')
        user = User.objects.create(**validate_data)
        Profile.objects.create(user=user, **profile)
        return user
