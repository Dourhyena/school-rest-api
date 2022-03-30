from django.contrib.auth.models import User
from .serializers import SignUpSerializer, MyTokenObtainPairSerializer, ChangePasswordSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class SignUpView(generics.CreateAPIView):

    """An endpoint used for registering user"""
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class MyTokenObtainPairView(TokenObtainPairView):

    """An endpoint for obtaining Access and Refresh Tokens"""
    serializer_class = MyTokenObtainPairSerializer

class ChangePasswordView(generics.UpdateAPIView):

    """An endpoint for changing password."""
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
