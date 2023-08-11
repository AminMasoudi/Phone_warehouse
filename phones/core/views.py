from django.views.generic import TemplateView
from .forms import LoginForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render


class NewPhoneView(TemplateView):
    template_name = "core/phones.html"

class AuthView(TemplateView):
    template_name = "core/auth.html"
    extra_context = {"form": LoginForm()}

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        user = form.auth(request)
        if user:
            login(request, user)  
            return HttpResponseRedirect("core:Phones")
        return render(request, 'core/auth.html', {"form": form})