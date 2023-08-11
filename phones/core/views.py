from django.views.generic import TemplateView
from django.urls import reverse_lazy

class NewPhoneView(TemplateView):
    template_name = "core/phones.html"

class AuthView(TemplateView):
    template_name = "core/auth.html"
    extra_context = {
        'api' : reverse_lazy('api:auth')
    }
