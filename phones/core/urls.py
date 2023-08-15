from django.urls import path
from . import views

app_name = "core"


urlpatterns = [
    path("new_phone/", views.PhoneCreateView.as_view(), name="New_Phone_view"),
    path("auth/", views.AuthView.as_view(), name="auth"),
    path("register/", views.RegisterView.as_view(), name="register")
    
]