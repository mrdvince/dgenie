from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User

from .auth import JWTAuth
from .serializers import UserSerializer


def valid_email(email):
    """Validate email.

    Args:
        email: email to validate
    Returns:
        True if valid, False otherwise
    """
    if "@" not in email:
        return False
    return True


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if not valid_email(data["email"]):
            raise exceptions.APIException("Invalid email")

        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("Passwords do not match")

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


register = RegisterAPIView.as_view()


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Incorrect password!")

        token = JWTAuth.generate_token(user.id)

        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"message": "Logged in successfully"}
        return response


login = LoginAPIView.as_view()


class UserAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


user_api_view = UserAPIView.as_view()


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def post(self, _):
        response = Response()
        response.delete_cookie(key="jwt")
        response.data = {"message": "Logged out successfully"}
        return response


logout = LogoutAPIView.as_view()


class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


user_info = ProfileInfoAPIView.as_view()


class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data
        if not user.check_password(data["old_password"]):
            raise exceptions.AuthenticationFailed("Incorrect password!")
        if data["new_password"] != data["new_password_confirm"]:
            raise exceptions.APIException("Passwords do not match")
        user.set_password(data["new_password"])
        user.save()
        return Response({"message": "Password changed successfully"})


user_password = ProfilePasswordAPIView.as_view()
