from django.forms import ModelForm, Form, CharField, PasswordInput, TextInput, EmailInput, NumberInput

from .models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Unique Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'age': NumberInput(attrs={'placeholder': 'Your age'})
        }


class LoginForm(Form):
    username = CharField(max_length=100, widget=TextInput(
        attrs={'placeholder': 'Username'}))
    password = CharField(max_length=255, widget=PasswordInput(
        attrs={'placeholder': 'Password'}))
