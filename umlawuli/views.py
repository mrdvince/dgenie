from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.auth import JWTAuth
from common.serializers import UserSerializer
from core.models import User


class AdminAPIView(APIView):

    authentication_classes = [JWTAuth]
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request):
        admins = User.objects.filter(is_superuser=True)
        serializer = UserSerializer(admins, many=True)
        return Response(serializer.data)


admin_api_view = AdminAPIView.as_view()


class GetUsersAPIView(APIView):
    authentication_classes = [JWTAuth]
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


users_api_view = GetUsersAPIView.as_view()
