from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Phone
from django.http import HttpResponseRedirect
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


class PhonesListView(ListView):
    model = Phone
    template_name = "core/phones_list.html"


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("core:phones"))
    return HttpResponseRedirect(reverse_lazy("core:auth"))