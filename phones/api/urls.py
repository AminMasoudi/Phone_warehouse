from django.urls import path
from . import views

app_name = "api"


urlpatterns = [
    path("phone/original", views.OriginalAPI.as_view(), name="Originals"),
    path("phone/nationality/<str:code>/", views.NationalityAPI.as_view(), name="Nationality"),

    path("phones/", views.PhoneAPI.as_view(), name="Phones_API"),
    path("brand/<str:code>", views.BrandsAPI.as_view(), name=""),

    path("auth/", views.AuthAPI.as_view(), name="auth"),
    path("register/", views.RegisterAPI.as_view(), name="register"),
]
