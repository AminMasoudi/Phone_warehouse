from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    PhoneSerializer,
    LoginSerializer,
    RegisterSerializer,
    BrandSerializer
)
from core.models import Phone, Brand, Country
from . import utils




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


class PhoneAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    


class BrandsAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSerializer

    def get(self, request, code):
        country = Country.objects.filter(code=code).first()
        if country :
            brands = Brand.objects.filter(country=country.pk).all()
            brands = BrandSerializer(brands, many=True)
            return Response(brands.data)

class OriginalAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        phones = Phone.objects.all()
        phones = list(filter(
            lambda x: utils.filter_by_nationality(x),
            phones
        ))
        phones = PhoneSerializer(phones, many=True)        
        return Response(phones.data)
    

class NationalityAPI(APIView):
    serializer_class = PhoneSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        country_code = kwargs["code"]
        country = Country.objects.filter(code=country_code).first()
        phones = Phone.objects.all()
        phones = list(filter(
            lambda x: utils.filter_by_nationality(x, country.name),
            phones
        ))
        phones = PhoneSerializer(phones, many=True)        
        return Response(phones.data)
