import datetime

import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from core.models import User
from dgenie import settings


class JWTAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Login expired")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed("Invalid token")

        user = User.objects.get(pk=payload["user_id"])

        if user is None:
            raise exceptions.AuthenticationFailed("User not found!")

        return user, token

    @staticmethod
    def generate_token(user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token
