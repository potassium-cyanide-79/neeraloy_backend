from rest_framework import generics
from .models import CustomUser
from .serializers import TenantSignupSerializer, LandlordSignupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TenantSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TenantSignupSerializer


class LandlordSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LandlordSignupSerializer


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer