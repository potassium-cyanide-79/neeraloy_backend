from django.urls import path
from .views import TenantSignupView, LandlordSignupView

urlpatterns = [
    path("signup/tenant/", TenantSignupView.as_view(), name="tenant-signup"),
    path("signup/landlord/", LandlordSignupView.as_view(), name="landlord-signup"),
]
