from django.urls import path
from . import views

app_name = "api"


urlpatterns = [
    path("add_phone/", views.NewPhoneAPI.as_view(), name="New_Phone_API"),
    path("auth/", views.AuthAPI.as_view(), name="auth")
]
