from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView

from rest_framework import status

from .serializers import UserRegistrationSerializer, UserProfileUpdateSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class CustomLoginView(ObtainAuthToken):
    # This view handles receiving a username and password.
    # If valid, it returns the Token + User Data (ID, Email, etc.)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        # I get or create the token for this user
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "email": user.email,
                "username": user.username,
            }
        )


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    # We override get_object so the URL doesn't need an ID (like /profile/5/).
    # Instead, DRF looks at the Token in the request, figures out who sent it and automatically grabs THAT specific user's profile.
    def get_object(self):
        return self.request.user
