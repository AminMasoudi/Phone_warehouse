
from django import forms
from django.contrib.auth import authenticate,login



class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65, required=True,widget=forms.PasswordInput)

    def auth(self,request):
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            return user
        return False
