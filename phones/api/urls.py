from django.urls import path
from . import views

app_name = "api"


urlpatterns = [
    path("phones/", views.PhoneAPI.as_view(), name="New_Phone_API"),
    path("auth/", views.AuthAPI.as_view(), name="auth"),
    path("register/", views.RegisterAPI.as_view(), name="register"),
    path("brands/<str:code>", views.BrandsAPI.as_view(), name="")
]
