from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", 'name', 'name_kana', )


class LoginForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", )
