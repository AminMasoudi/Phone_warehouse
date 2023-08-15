from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Phone
class NewPhoneView(TemplateView):
    template_name = "core/phones.html"

class AuthView(TemplateView):
    template_name = "core/auth.html"
    extra_context = {
        'api' : reverse_lazy('api:auth')
    }


class RegisterView(TemplateView):
    template_name = "core/register.html"
    extra_context = {
        'api' : reverse_lazy('api:register')
    }


class PhoneCreateView(CreateView):
    model = Phone
    template_name = "core/new_phone.html"
    fields= "__all__"
