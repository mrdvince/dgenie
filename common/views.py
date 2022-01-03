from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
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
