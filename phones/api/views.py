from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import PhoneSerializer, LoginSerializer, RegisterSerializer

class NewPhoneAPI(APIView):
    # authentication_classes = SessionAuthentication
    # permission_classes = IsAuthenticated

    def post(self, requests, *args, **kwargs):
        form = PhoneSerializer(data=requests.data)
        form.is_valid(raise_exception=True)
        form.save()


class AuthAPI(APIView):

    def post(self, request, format=None):
        login_ser = LoginSerializer(User, data=request.data)
        login_ser.is_valid(raise_exception=True)
        user = authenticate(request,
                            username=login_ser.validated_data.get("username"),
                            password=login_ser.validated_data.get("password"))
        if user:
            login(request, user)
            return Response(login_ser.validated_data.get("username"))
        return Response({
            "detail": "failed to log in"
        }, 401)

class RegisterAPI(APIView):

    def post(self, request, format=None):
        register_ser = RegisterSerializer(data=request.data)
        register_ser.is_valid(raise_exception=True)
        user = register_ser.save()
        login(request ,user)
        return Response(register_ser.validated_data)
