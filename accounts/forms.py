from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("full_name", "phone", "address", "avatar")
