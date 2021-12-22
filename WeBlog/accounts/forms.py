from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# from accounts.models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label='username', widget=forms.TextInput(
        attrs={'class': 'username__input form__input', 'placeholder': 'Username...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'password__input form__input', 'placeholder': '••••••••••'}))

    class Meta:
        model = User
        fields = ['username', 'password']


# class UserDetailForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'bio', 'profile_pic']
