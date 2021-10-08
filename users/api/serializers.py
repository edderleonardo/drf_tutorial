from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]

    def validate_email(self, email):
        email_domain = email.split('@')[1]

        if email_domain == 'yahoo.com':
            raise serializers.ValidationError(
                "No permitimos el registro con una cuenta de Yahoo")
        return email
