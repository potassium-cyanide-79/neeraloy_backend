from django.urls import path
from .views import (
    TenantSignupView,
    LandlordSignupView,
    LoginView,
)

urlpatterns = [
    path("signup/tenant/", TenantSignupView.as_view(), name="tenant-signup"),
    path("signup/landlord/", LandlordSignupView.as_view(), name="landlord-signup"),
    path("login/", LoginView.as_view(), name="login"),
]
