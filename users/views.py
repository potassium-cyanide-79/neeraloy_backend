from rest_framework import generics
from .models import CustomUser
from .serializers import TenantSignupSerializer, LandlordSignupSerializer


class TenantSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TenantSignupSerializer


class LandlordSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LandlordSignupSerializer
