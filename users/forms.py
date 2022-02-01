from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CreateUserForm(UserCreationForm):
  email = forms.EmailField(max_length=250, help_text="Don't enter a random email. Enter the email that you use frequently.")
  
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

class UpdateUserForm(UserChangeForm):
  class Meta:
    model = User
    fields = ("username", "email")

class UpdateUserProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ("bio", "image")
